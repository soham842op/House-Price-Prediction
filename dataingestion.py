import os
import zipfile
import pandas as pd
from abc import ABC,abstractmethod

#Following the steps of the Factory Design File (Coffee House Example to understand it again) 


class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path:str)->pd.DataFrame:
        '''Abstract Method to ingest data from a given file'''
        pass

#Implement a concrete class for ZIP ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path)-> pd.DataFrame :
        if not file_path.endswith('.zip'):
            raise ValueError("Provided file isn't a zip file")
        

        #Extract the zip file
        with zipfile.ZipFile(file_path,'r') as zip_ref:          #zip_ref is reference of the content and is stored in the folder extracted_data
            zip_ref.extractall('extracted_data')

        extracted_files=os.listdir('extracted_data')
        csv_files=[f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files)==0:
            raise FileNotFoundError("No CSV file found in the extracted data folder")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files are found in the extraced data folder .Please specify which one to use")
        

        #Read the CSV into a DataFrame
        csv_file_path=os.path.join('extracted_data',csv_files[0])
        df=pd.read_csv(csv_file_path)

        return df
    

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str)->DataIngestor:
        #Returns The Appropriate DataIngestor based on file extension
        if file_extension ==".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f'No ingestor available for file extension:{file_extension}')
        

if __name__=="__main__":

    file_path="data/archive.zip"

    file_extension=os.path.splitext(file_path)[1]

    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    df=data_ingestor.ingest(file_path)

    print(df.head())

    pass



