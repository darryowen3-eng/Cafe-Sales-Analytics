from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_file('mary shavin/dirty_cafe_sales', 'cafe_sale.csv', path='./')

