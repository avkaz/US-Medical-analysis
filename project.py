# -*- coding: utf-8 -*-
import csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

#function to load csv_data into lists
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst

# look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class patientsInfo:
    
    # constuctor for patients information
    def __init__(self, ages, sexes, bmis, num_children, smokers, regions, insurances):
        
        self.ages = ages
        self.sexes = sexes
        self.bmis = bmis
        self.num_children = num_children
        self.smokers = smokers
        self.regions = regions
        self.insurances = insurances
        
    # method that returns information about ages of patients in database
    def ages_info(self):
        
        total_age = 0
        highest_age=0
        lowest_age=100
        #average age 
        for i in self.ages:
            total_age+= int(i)
            #highest age
            
            for i in self.ages:
                if int(highest_age) < int(i):
                    highest_age=i
                else: continue
            
            #lowest_age
            
            for i in self.ages:
                if int(i) < int(lowest_age):
                    lowest_age=i
                else: continue
        print('Average Patient Age: {av_age} years.'.format(av_age = round(total_age/len(self.ages), 2)))
        print('The oldest patient is {highest_age} years old.'.format(highest_age=highest_age))
        print('The youngest patient is {lowest_age} years old.'.format(lowest_age=lowest_age))
        print(' ')       
       
    # method that returns information about sexes of patients in database
    def sex_info(self):
        men_count=0
        women_count=0
        # count of men and women in the database
        for i in self.sexes:
            if i =='male':
                men_count+=1
            elif i =='female':
                women_count+=1
            else:
                continue
        #percentage of men and women from total amount
        men_percentage=men_count/len(self.sexes)
        women_percentage=women_count/len(self.sexes)
        print("Count for male: " , men_count , ', ' , round(men_percentage*100,2) , '%')
        print("Count for female: " , women_count , ', ' , round(women_percentage*100,2) , '%')
        print(' ')    
     
    # method that returns information about regions of patients in database
    def regions_info(self):
        #unigue regions 
        unique_regions=[]
        for i in self.regions:
            if i  not in unique_regions:
                unique_regions.append(i)
            else:continue
        print('Regions: ', unique_regions)
        # accurance of each unique value in the list of regions
        regions_count={}
        for i in self.regions:
            if i in regions_count:
                regions_count[i] +=1
            else: regions_count[i] = 1
        for i in regions_count:
            print(i,': ', regions_count[i])
        print(' ')
            
    def insurance_info(self):
        charges_total=0
        for i in self.insurances:
            charges_total+=float(i)
        return ('Average Yearly Medical Insurance Charges:' + str(round(charges_total/len(self.insurances),2)) + ' dollars.')
        
        
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.ages]
        self.patients_dictionary["sex"] = self.sexes
        self.patients_dictionary["bmi"] = self.bmis
        self.patients_dictionary["children"] = self.num_children
        self.patients_dictionary["smoker"] = self.smokers
        self.patients_dictionary["regions"] = self.regions
        self.patients_dictionary["charges"] = self.insurances
        return self.patients_dictionary
    
patient_info = patientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.ages_info()    
patient_info.sex_info()    
patient_info.regions_info()
patient_info.insurance_info()
patient_info.create_dictionary()

            
