# This is a coding assignment from another company as part of their technical review process. This was sent as a "take home" challenge.

# see graphic in instructions for visual explanation of the permission and user data structures
class Authorization:
  def __init__(self, permissions, users):
    self.permissions = permissions
    self.users = users

# @rtype: list of strings
# @returns: a list of all the active permission names that the user with the corresponding user_id has
# @note: The order in which the permission names are returned is not important
# @example: listPermissions(1) ➡ ["Lock User Account", "Unlock User Account"] (purchased widgets not included since it is not active)
  def list_permissions(self, user_id):
    # set role; if not found to return error message.
    roles = []
    roles_list = []

    # enter list
    for x in self.users:
      # find correct dictionary key/value pair, if it exists
      if user_id == x["id"]:
        roles = x["roles"]

    #print(roles)
    
    # throw exception if the user_id isn't found.
    if len(roles) == 0:
      return "Error: user_id not found!"

    # enter list
    for y in roles:
      # find matching key/value pair and check that the attribute is active.
      for z in self.permissions:
        if z["role"] == y and z["active"] == True:
          roles_list.append(z["name"])

    if len(roles_list) == 0:
      return "Error: role not found! No permissions granted"

    return roles_list

# @rtype: boolean value
# @returns: true or false based on if the user with the corresponding user_id has the role that corresponds with the specific permission_name and that particular permission is active
# @example: Example (Based on data from graphic)
# checkPermitted("scooters near me", 2) ➡ true
# checkPermitted("scooters near me", 1) ➡ false
  def check_permitted(self, permission_name, user_id):
    # set return value to false until proven otherwise
    perms_bool = False

    # get list of permissions from class function
    perms = self.list_permissions(user_id)

    # check if the permission_name is in the permission list, perms; set to True if it is.
    for x in perms:
      if x == permission_name:
        perms_bool = True

    return perms_bool

# Main
if __name__ == '__main__':
    permissions = [
      { "role": "superuser", "name": "lock user account", "active": True },
      { "role": "superuser", "name": "unlock user account", "active": True },
      { "role": "superuser", "name": "purchase widgets", "active": False },
      { "role": "charger", "name": "view pick up locations", "active": True },
      { "role": "rider", "name": "view my profile", "active": True },
      { "role": "rider", "name": "scooters near me", "active": True },
    ]

    users = [
      { "id": 1, "name": "Anna Administrator", "roles": ["superuser"] },
      { "id": 2, "name": "Charles N. Charge", "roles": ["charger", "rider"] },
      { "id": 7, "name": "Ryder", "roles": ["rider"] },
      { "id": 11, "name": "Unregistered Ulysses", "roles": [] },
      { "id": 18, "name": "Tessa Tester", "roles": ["beta tester"] },
    ]

    test = Authorization(permissions, users)

    print(test.list_permissions(1))
    print(test.list_permissions(2))
    print(test.list_permissions(5))
    print(test.list_permissions(11))
    print(test.list_permissions(18))


    print(test.check_permitted("scooters near me", 2))
    print(test.check_permitted("view pick up locations", 1))
    print(test.check_permitted("scooters near me", 18))

    
