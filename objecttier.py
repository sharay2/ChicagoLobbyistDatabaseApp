#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self): return self._Lobbyist_ID

   @property
   def First_Name(self): return self._First_Name

   @property
   def Last_Name(self): return self._Last_Name

   @property
   def Phone(self): return self._Phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = Years_Registered
      self._Employers = Employers
      self._Total_Compensation = Total_Compensation

   @property
   def Lobbyist_ID(self): return self._Lobbyist_ID
   @property
   def Salutation(self): return self._Salutation
   @property
   def First_Name(self): return self._First_Name
   @property
   def Middle_Initial(self): return self._Middle_Initial
   @property
   def Last_Name(self): return self._Last_Name
   @property
   def Suffix(self): return self._Suffix
   @property
   def Address_1(self): return self._Address_1
   @property
   def Address_2(self): return self._Address_2
   @property
   def City(self): return self._City
   @property
   def State_Initial(self): return self._State_Initial
   @property
   def Zip_Code(self): return self._Zip_Code
   @property
   def Country(self): return self._Country
   @property
   def Email(self): return self._Email
   @property
   def Phone(self): return self._Phone
   @property
   def Fax(self): return self._Fax
   @property
   def Years_Registered(self): return self._Years_Registered
   @property
   def Employers(self): return self._Employers
   @property
   def Total_Compensation(self): return self._Total_Compensation
   

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   @property
   def Lobbyist_ID(self): return self._Lobbyist_ID
   @property
   def First_Name(self): return self._First_Name
   @property
   def Last_Name(self): return self._Last_Name
   @property
   def Phone(self): return self._Phone
   @property
   def Total_Compensation(self): return self._Total_Compensation
   @property
   def Clients(self): return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   sql = """
      SELECT COUNT(Lobbyist_ID)
      FROM LobbyistInfo
         """
   try:
      # counts the number of lobbyists by their IDs (given that each ID is unique)
      results = datatier.select_one_row(dbConn,sql)
      return results[0]
   except Exception as err:
      print("num_lobbyists failed:", err)
      return -1

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   sql = """
      SELECT COUNT(Employer_ID)
      FROM EmployerInfo
         """
   try:
      # counts the number of employers by their IDs (given that each ID is unique)
      results = datatier.select_one_row(dbConn,sql)
      return results[0]
   except Exception as err:
      print("num_employers failed:", err)
      return -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   sql = """
      SELECT COUNT(Client_ID)
      FROM ClientInfo
         """
   try:
      # counts the number of clients by their IDs (given that each ID is unique)
      results = datatier.select_one_row(dbConn,sql)
      return results[0]
   except Exception as err:
      print("num_clients failed:", err)
      return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   # sql query for finding Lobbyist_ID, First_Name, Last_Name, Phone
   sql = """
      SELECT Lobbyist_ID, First_Name, Last_Name, Phone
      FROM LobbyistInfo
      WHERE Last_Name LIKE ? OR First_Name LIKE ?
      ORDER BY Lobbyist_ID ASC
         """
   try:
      results = datatier.select_n_rows(dbConn,sql,[pattern,pattern])

      lobbyList = []
      for rows in results:
         # create a Lobbyist object for each lobbyist and store them in an array
         id, fName, lName, phone = rows
         temp = Lobbyist(id,fName, lName, phone)
         lobbyList.append(temp)
      #return list of lobbyists objects
      return lobbyList
   except Exception as err:
      print("get_lobbyists failed:", err)
      return []


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   # sql query for finding Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation
   sql_info = """
      SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax
      FROM LobbyistInfo
      WHERE Lobbyist_ID = ?
         """
   # sql query for finding lobbyist year
   sql_year = """
      SELECT Year
      FROM LobbyistYears
      WHERE Lobbyist_ID = ?
      ORDER BY Year ASC
         """
   # sql query for finding lobbyist's compensation
   sql_comp = """
      SELECT SUM(Compensation_Amount)
      FROM Compensation
      WHERE Lobbyist_ID = ?
         """
   # sql query for find lobbyist's employers
   sql_employers = """
      SELECT DISTINCT EmployerInfo.Employer_Name
      FROM EmployerInfo
      JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
      WHERE LobbyistAndEmployer.Lobbyist_ID = ?
      ORDER BY Employer_Name ASC
         """
   try:
      # run all sql queries
      info = datatier.select_one_row(dbConn, sql_info, [lobbyist_id])
      years = datatier.select_n_rows(dbConn, sql_year, [lobbyist_id])
      comp = datatier.select_one_row(dbConn, sql_comp, [lobbyist_id])
      emp = datatier.select_n_rows(dbConn, sql_employers, [lobbyist_id])
      # return when lobbyist isn't found
      if not info:
         return None
      # set compensation to 0 if none is found
      if comp is None or comp[0] is None:
         compensation = 0.0
      else:
         compensation = comp[0]
      # dissecting the results into their respective parts
      id, sal, fname, midinitial, lname, suf, add1, add2, city, state, zipcode, country, email, phone, fax = info
      employers = []
      yearsList = []
      for row in emp: # finds list of employers
         eName = row[0]
         employers.append(eName)
      for row in years: # finds list of years
         y = row[0]
         yearsList.append(y)
      # create a LobbyistDetails object and return it
      lobbyist_details = LobbyistDetails(id, sal, fname, midinitial, lname, suf, add1, add2, city, state, zipcode, country, email, phone, fax, yearsList, employers, compensation)
      return lobbyist_details
   except Exception as err:
      print("get_lobbyist_details failed:",err)
      return None

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   # sql query for finding the top N lobbyists based on compensation
   top_sql = """
      SELECT LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, SUM(Compensation_Amount) AS Comp
      FROM LobbyistInfo
      JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
      WHERE strftime('%Y', Period_Start) = ?
      GROUP BY Compensation.Lobbyist_ID
      ORDER BY Comp DESC
      LIMIT ?
         """
   # sql query for finding the top lobbyist's clients
   client_sql = """
      SELECT Client_Name
      FROM ClientInfo
      JOIN Compensation ON ClientInfo.Client_ID = Compensation.Client_ID
      WHERE strftime('%Y', Period_Start) = ? AND Compensation.Lobbyist_ID = ?
      GROUP BY Compensation.Client_ID
      ORDER BY Client_Name ASC
         """
   
   try:
      topresults = datatier.select_n_rows(dbConn, top_sql, [year, N])
      if topresults is None:
         return []
      
      toplobbyists = []
      for row in topresults:
         # dissecting information from sql query
         id, lobbyfname, lobbylname, phone, comp = row
         clients = []
         results = datatier.select_n_rows(dbConn, client_sql,[year, id])
         # storing a lobbyist's clients into a list
         for cl in results:
            clients.append(cl[0])
         # create a LobbyistClients object to store the lobbyist's information and their clients
         temp = LobbyistClients(id, lobbyfname, lobbylname, phone, comp, clients)
         toplobbyists.append(temp)
      # return the top N lobbyists in the form of LobbyistClients objects
      return toplobbyists
   except Exception as err:
      print("get_top_N_lobbyists failed:", err)
      return []

##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   # sql query for finding if the lobbyist exists
   sql_check = """
      SELECT COUNT(*)
      FROM LobbyistInfo
      WHERE Lobbyist_ID = ?
         """
   # sql query for inserting a year for the lobbyist
   sql_insert = """
      INSERT INTO LobbyistYears (Lobbyist_ID, Year)
      VALUES (?,?)
         """
   
   try:
      # check if lobbyist exists
      check = datatier.select_one_row(dbConn, sql_check, [lobbyist_id])
      if check[0] == 0:
         return 0
      # insert year for the specified lobbyist
      add = datatier.perform_action(dbConn, sql_insert, [lobbyist_id, year])
      if add <= 0:
         return 0
      
      return 1
   except Exception as err:
      print("add_lobbyist_year failed:", err)
      return 0


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   # sql query for finding if the lobbyist exists
   sql_check = """
      SELECT COUNT(*)
      FROM LobbyistInfo
      WHERE Lobbyist_ID = ?
         """
   # sql query for updating a lobbyist's salutation
   sql_salutation = """
      UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?
         """
   
   try:
      # check if lobbyist exists
      check = datatier.select_one_row(dbConn, sql_check, [lobbyist_id])
      if check[0] == 0:
         return 0
      # update salutation for the specified lobbyist
      update = datatier.perform_action(dbConn, sql_salutation, [salutation, lobbyist_id])
      if update <= 0:
         return 0
      
      return 1
   except Exception as err:
      print("set_salutation failed:", err)
      return 0


def get_order_details(dbConn, id):
   dbCursor = dbConn.cursor()
   sql = """
      SELECT OID
      FROM OrderDetails
      WHERE OID = ?
         """

   try:
      dbCursor.execute(sql,[id])
      result = dbCursor.fetchall()
      return result
   except Exception as err:
      print("Error:", err)
      return -1