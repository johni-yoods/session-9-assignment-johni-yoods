Name : Johni Yoods Durai
email : durai.mj@mistralsolutions.com

# Session 9

## Named Tuple

## Random Profiles
Using faker library generated 10000 random profiles. And the largest blood group, oldest person's age from the
profiles will be calcualted using named tuple and dictionary method


 ### create random profiles and stored it in a named tuple
        self.profiles = namedtuple('profiles',fake.profile().keys())
        self.group = namedtuple('group',['profiles'])

        for i in range(10000):
            p1 = self.profiles(**fake.profile())
            if(i==0):
                self.profiles_nt = self.group(p1)
            else:
                self.profiles_nt += self.group(p1)

### create random profiles and stored it in a named tuple
        self.profiles=[]
        for i in range(10000):
            self.profiles.append(fake.profile())
            
# find largest blood group 
count the blood group and update the dictionary value for all the profiles. Finally return the largest blood group.
### def largest_bloodgroup(self):
        blood_group = {}
        for prof in self.profiles:
            bg = prof['blood_group']
            if bg not in blood_group:
                 blood_group[bg]=0
            else:
                 blood_group[bg]+=1
        prev_count = 0
        for i in blood_group:
            count = blood_group[i]
            if count>prev_count:
                prev_count = count
                most_bg = i

        return most_bg

# Find Oldest person age
Using the birth date calculate the age for all the profiles and find the oldest person's age
### def oldest_person(self):

        current_year = int(str(datetime.date.today())[:4])
        oldest_year = current_year
        for prof in self.profiles:
            year = int(str(prof['birthdate'])[:4])
            if year<oldest_year:
                oldest_year = year
        oldest_person_age = current_year-oldest_year
        return oldest_person_age
# Find average age
Using the birth date calculate the age for all the profiles and find the average of them
### def average_age(self):
        current_year = int(str(datetime.date.today())[:4])
        avg_age = 0
        no = 0
        for prof in self.profiles:
            year = int(str(prof['birthdate'])[:4])
            age = current_year - year
            avg_age = (avg_age+age)
            no+=1
        return avg_age/no
# Find the mean location
In the given profies find the mean location value from the all values
### def mean_location(self):
       mean_x = 0
       mean_y = 0
       no = 0
       for prof in self.profiles:
            x,y = (prof['current_location'])
            mean_x,mean_y = (mean_x + x),(mean_y+y)
            no+=1
       return mean_x/no,mean_y/no

