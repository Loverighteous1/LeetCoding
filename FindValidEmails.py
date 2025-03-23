
import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """
    Description:
        Given a pandas dataframe which has two columns: user_id and email, 
        write a solution to find all the valid email addresses.
        
        (user_id) is the unique key for this table.
        Each row contains a user's unique ID and email address.
         
        A valid email address meets the following criteria:
            * It contains exactly one @ symbol.
            * It ends with .com.
            * The part before the @ symbol contains only alphanumeric characters and underscores.
            * The part after the @ symbol and before .com contains a domain name that contains only
                letters.

        Return the result table ordered by user_id in ascending order.
            """
   
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphanumeric = letters + "0123456789"
    
    valid_email = pd.DataFrame(columns=["user_id", "emails"])
    for idx, (idd, eml) in enumerate(zip(users["user_id"], users["emails"])):
        email = eml
        split_hat = email.split("@")
        split_com = email.split(".com")

        if (len(split_hat) == 2) and (len(split_com) == 2):
            
            for car in split_hat[0]:
                if car in alphanumeric:
                    continue
            
            split_dot = split_hat[1].split('.')
            for let in split_dot[0]:
                if let in letters:
                    continue
            
            if split_dot[1] == "com":
                com = "end"
            valid_email.loc[len(valid_email)] = [idd, eml]
    return valid_email
    
### Test
dic = {"user_id": [1, 2, 3, 4, 5],
        "emails": ['alice@example.com', 'bob_at_example.com', 'charlie@example.net', 'david@domain.com', 'eve@invalid']
}

data = pd.DataFrame(dic)
data

valid_emails = find_valid_emails(data)
print(valid_emails)