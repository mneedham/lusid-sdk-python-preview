# IrVolCubeData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the cube - this is the start date of the swaptions on the cube. | 
**instruments** | [**list[LusidInstrument]**](LusidInstrument.md) | Retrieve the set of instruments that define the cube. | 
**quotes** | [**list[MarketQuote]**](MarketQuote.md) | Access the set of quotes that define the cube. | 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


