from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_splitter_step import data_splitter_step
from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path="data/archive.zip"
    )

    # Handling Missing Values Step
    filled_data = handle_missing_values_step(raw_data)

    #Feature Engineering Step
    engineeered_data=feature_engineering_step(filled_data,strategy='log',features=["Gr Liv Area","SalePrice"])


    #Outlier Detection Step
    clean_data=outlier_detection_step(engineeered_data,column_name="SalePrice")

    #Data Splitting Step
    #80% and 20% split for train and test
    X_train,X_test,y_train,y_test=data_splitter_step(clean_data,target_column="SalePrice")

    #Model building Step
    


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()


