def get_text_analytics(text = None, return_type = None):
    """
    return_types: "sentiment_score, sentiment_confidence"
    """
    
    def get_config():
        """
        get azure cognitive services connection information and api keys|
        fqdn = fully qualified domain name
        """
        textconfig = {
            "cog_services_resource_name": config["AZURE_COG_SERVICES_RESOURCE_NAME"],
            "cog_services_api_key": config["AZURE_COG_SERVICES_API_KEY"],
            "cog_services_base_url": config["AZURE_COG_SERVICES_BASE_URL"]
        }
        textconfig["fqdn"] = "https://" + textconfig["cog_services_resource_name"] + "." + textconfig["cog_services_base_url"]
        return textconfig


    def get_text_analytics_client(config = None):
        """
        get azure cognitive services text analytics client
        """
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.textanalytics import TextAnalyticsClient
        creds = AzureKeyCredential(config["cog_services_api_key"])
        text_analytics_client = TextAnalyticsClient(endpoint = config["fqdn"], credential = creds)
        return text_analytics_client


    def get_text_analytics_sentiment(config = None, text = None):
        """
        get text analytics sentiment for a line of text in a python list
        """
        if text == None: text_list = ["NA"]
        else: text_list = [text] 
        sentiment_response = get_text_analytics_client(config).analyze_sentiment(text_list)
        return sentiment_response

    
    def get_text_analytics_keyphrases(config = None, text = None):
        """
        get text analytics keyphrases for a line of text in a python list
        """
        if text == None: text_list = ["NA"]
        else: text_list = [text] 
        keyphrase_response = get_text_analytics_client(config).extract_key_phrases(text_list, language = "en")
        return keyphrase_response
    
    
    # keyphrases
    if return_type == "keyphrases":
        return get_text_analytics_keyphrases(config = get_config(), text = text)[0].key_phrases
    
    # overall sentiment
    if return_type == "sentiment_overall":
        return get_text_analytics_sentiment(config = get_config(), text = text)[0].sentiment
    
    # sentiment confidence
    if return_type == "sentiment_confidence":
        conf = get_text_analytics_sentiment(config = get_config(), text = text)[0].confidence_scores
        pos = conf.positive
        neut = conf.neutral
        neg = conf.negative
        return [pos, neut, neg]


# make text analytics python user defined function (UDF)
textanalyticsUDF = udf(lambda a, b: get_text_analytics(a, b), StringType())


def read_delta_table_spark(datapath = None, filename = None):
    """
    read delta table into spark dataframe
    """
    return spark.read.load(datapath + "/" + filename, format = "delta")


def add_text_analytics_columns(df = None, colnames = None):
    """
    add all text analytics columns to spark dataframe for all dataframe text fields dynamically
    """
    for col in colnames:
        df = df \
            .withColumn(col + "_Keyphrases", textanalyticsUDF(F.col(col), F.lit("keyphrases"))) \
            .withColumn(col + "_Sentiment", textanalyticsUDF(F.col(col), F.lit("sentiment_overall"))) \
            .withColumn(col + "_Confidence", textanalyticsUDF(F.col(col), F.lit("sentiment_confidence")))
    return df
    


# read ps engagement delta tables into spark dataframes
datapath_pre = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTfYIpa3l0od5xV3j0kxmjZPYFmY5Gm7QLFuod_SIlplTlXcnW7Mk4vaIcZOGX_kAr0NdvBjPCmQ6zc/pub?output=csv"
datapath_active = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQELi61POwMVyLfTS9CR9KraaDmJsUZlg2SCwsAxcodXv4H7JamJLxzCWAZOE32xTTjMm1JAAXKfoxa/pub?output=csv"
datapath_post = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSDFmTMjHS_TlY5wdlLBWufzldwy7UBJL74G-DAvJLFHqq0pyvWCblReP4HHQF5YvTMh9GSCom86xa-/pub?output=csv"


# make local copies of the data files
localpath_base = "/data/ps_metrics"
filename_pre = "pre_engagement_responses.csv"
filename_active = "active_engagement_responses.csv"
filename_post = "post_engagement_responses.csv"

# create directories if they don't exist
if 


pre_data_df = read_delta_table_spark(data_path, filename = "pre_engagement_responses")
active_data_df = read_delta_table_spark(data_path, filename = "active_engagement_responses")
post_data_df = read_delta_table_spark(data_path, filename = "post_engagement_responses")


# pre engagement commentary fields + text analytics
pre_engage_filename = "Pre_Engagement_Responses_TextAnalytics"
pre_text_cols = ["Snowflake_Compete"]
pre_data_df = add_text_analytics_columns(pre_data_df, pre_text_cols)
pre_data_df.write.mode("overwrite").saveAsTable(pre_engage_filename)


# active engagement commenary fields + text analytics
active_engage_filename = "Active_Engagement_Responses_TextAnalytics"
active_text_cols = ["Client_Responsive", "Expectations_ProjRequire_Align", "Customer_Team_Executing_Well"]
active_data_df = add_text_analytics_columns(active_data_df, active_text_cols)
active_data_df.write.mode("overwrite").saveAsTable(active_engage_filename)


# # post engagement commentary fields + text analytics
post_engage_filename = "Post_Engagement_Responses_TextAnalytics"
post_text_cols = ["More_Lakehouse_Adoption", "New_Use_Cases", "Capture_Success_Story", "Additional_Feedback", "Reusable_Project_Components", "Project_Successful", "Databricks_Company_Goals_Achieved"]
post_data_df = add_text_analytics_columns(post_data_df, post_text_cols)
post_data_df.write.mode("overwrite").saveAsTable(post_engage_filename)