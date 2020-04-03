import looker_sdk

sdk = looker_sdk.init31()

result = sdk.run_inline_query(result_format='json',apply_formatting=False,cache=False,server_table_calcs=False,body=looker_sdk.models.WriteQuery(
	model= "wix",
	view= "api_call",
    fields= ['api_call.is_current_period', 'api_call.orders', 'api_call.total_revenue', 'api_call.products', 'api_call.visitors_count', 'api_call.new_visitors_count'],
    filters= {
      "api_call.time_periods": "90days",
      "api_call.comparison_period": "previousPeriod",
      "api_call.tenant_id": "a088f6a8-01e1-45e5-87c9-4fc48a28597e"
    },
    limit= 10,
    query_timezone= "UTC"
))

print(result)