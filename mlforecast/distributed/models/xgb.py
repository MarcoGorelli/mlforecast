# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/distributed.models.xgb.ipynb (unless otherwise specified).

__all__ = ['XGBForecast']

# Cell
import xgboost as xgb


# Cell
class XGBForecast(xgb.dask.DaskXGBRegressor):

    @property
    def model_(self):
        return self.get_booster()