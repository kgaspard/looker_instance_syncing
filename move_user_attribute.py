import looker_sdk

sdk = looker_sdk.init31()

def get_developer_user_ids():
  admin_role_id = sdk.search_roles(name='Admin',fields='id')
  developer_role_id = sdk.search_roles(name='Developer',fields='id')
  admin_user_ids = [user.id for user in sdk.role_users(role_id=admin_role_id[0].id, fields='id', direct_association_only=True)]
  developer_user_ids = [user.id for user in sdk.role_users(role_id=developer_role_id[0].id, fields='id', direct_association_only=True)]
  return admin_user_ids + developer_user_ids


user_attributes = [user_attribute.name for user_attribute in sdk.all_user_attributes(fields='name')]
if('can_see_api_explore' not in user_attributes):
  sdk.create_user_attribute(body={
    "name": 'can_see_api_explore',
    "label": 'Can See API Explore',
    "type": 'string',
    "default_value": 'no',
    "value_is_hidden": False,
    "user_can_view": True,
    "user_can_edit": False
  })
  print("Created user attribute can_see_api_explore")

can_see_api_explore_user_attribute_id = -1
new_user_attributes = sdk.all_user_attributes(fields='id,name')
for user_attribute in new_user_attributes:
  if(user_attribute.name == 'can_see_api_explore'):
    can_see_api_explore_user_attribute_id = int(user_attribute.id)

for user_id in get_developer_user_ids():
  sdk.set_user_attribute_user_value(user_id=user_id,user_attribute_id=can_see_api_explore_user_attribute_id,body=looker_sdk.models.WriteUserAttributeWithValue(value="yes"))