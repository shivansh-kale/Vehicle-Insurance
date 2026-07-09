import sys

import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.exception import MyException
from src.logger import logging


# Maps target class names to numeric values and vice versa
class TargetValueMapping:

    def __init__(self):
        # Target label encoding
        self.yes: int = 0
        self.no: int = 1

    # Return mapping as a dictionary
    def _asdict(self):
        return self.__dict__

    # Return reverse mapping (0 -> yes, 1 -> no)
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


# Wrapper class that combines the preprocessing pipeline and trained model
class MyModel:

    def __init__(self,
                 preprocessing_object: Pipeline,
                 trained_model_object: object):
        """
        preprocessing_object : Fitted preprocessing pipeline
        trained_model_object : Trained machine learning model
        """

        # Store the preprocessing pipeline
        self.preprocessing_object = preprocessing_object

        # Store the trained model
        self.trained_model_object = trained_model_object

    # Apply preprocessing and generate predictions
    def predict(self, dataframe: pd.DataFrame) -> DataFrame:
        try:
            logging.info("Starting prediction process.")

            # Transform raw input data using the fitted preprocessing pipeline
            transformed_feature = self.preprocessing_object.transform(dataframe)

            # Generate predictions using the trained model
            logging.info("Using the trained model to get predictions")
            predictions = self.trained_model_object.predict(transformed_feature)

            # Return predicted values
            return predictions

        except Exception as e:
            logging.error("Error occurred in predict method", exc_info=True)
            raise MyException(e, sys) from e

    # String representation for debugging
    def __repr__(self):                                             #Returns : RandomForestClassifier()
        return f"{type(self.trained_model_object).__name__}()"

    # String representation when printed
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"