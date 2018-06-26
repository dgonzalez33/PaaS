
    
class User():
    def __init__(self, file_location ='passwd.txt' ):
        self.file_location = file_location
        #comma seperated headers in passwd file
        self.format = ["name","encryption","uid","gid","comment","home","shell"]
    def parseFile(self):
        """ Read the raw passwd file and parse it to a usable array of dicts"""
        users = []
        with open(self.file_location) as passwd_file:
            for line in passwd_file:
                line = line.strip()
                user = line.split(":")
                users.append( {self.format[i] : user[i] for i in range(len(user)) } )
        return users
    def query(self, params):
        """ Query the passwd file based on a set of parameters. If an invalid parameter is passed,
            no user will pass the filter"""
        parsed_users = self.parseFile()
        filtered_users = []
        for user in parsed_users:
            isFiltered = True
            for key, value in params.items():
                if(key not in user.keys() or user[key] != value):
                    isFiltered = False
                    break
            if(isFiltered):
                filtered_users.append(user)
        return filtered_users

class Group():
    def __init__(self, file_location = 'group.txt'):
        self.file_location = file_location
        self.format = ["name","password","gid","members"]
    def parseFile(self):
        """ Read the raw groups file and parse it to a usable array of dicts"""
        groups = []
        with open(self.file_location) as group_file:
            for line in group_file:
                line = line.strip()
                group = line.split(":")
                group[3] = group[3].split(",")
                groups.append( {self.format[i] : group[i] for i in range(len(group)) } )
        return groups
    def query(self, params):
        """ Query the groups file based on a set of parameters. If an invalid parameter is passed,
            no user will pass the filter"""
        parsed_list = self.parseFile()
        filtered_groups = []
        for item in parsed_list:
            isFiltered = True
            # if members is a query pam, check if members within params are in members of groups
            if "member" in params.keys():
                for member in params["member"]:
                    if member not in item["members"]:
                        isFiltered = False  
                        break
            for key, value in params.items():
                # Don't want to check the member key, since it is different that members key in groups file.
                if(key == "member"):
                    continue
                if(key not in item.keys() or item[key] != value):
                    isFiltered = False
                    break
            if(isFiltered):
                filtered_groups.append(item)
        return filtered_groups


    
