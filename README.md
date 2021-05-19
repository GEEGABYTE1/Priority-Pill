# Patient Database 🩺

Automate prioritizing patients based on medical needs without machine learning. Can be used for expiremental cases and in real-time hospitals. 


# User Database Information 

When the user first launches the program, they will be encountered with a "database" where they must create their hospital's personal patient database. After that, they can go and launch the software's main feature.

Users can create up to 9 patient databases for unique hospitals. 

If the user creates another database with the same hospital name, it will override the old database with the same hospital name. This is because of the fact that this user database in general runs under a *hash map* data structure to improve performance and convenience. 

Most operations run linear time.


# Patient Database Information

A Patient Database that prioritizes patients based on their medical needs and issues 🩺

This software prioritizes patients based on values that have been defined by the user itself based on their medical attention. Without the use of a machine learning model, the priority queue does the prioritizing.

Since the user can make up the priority value based on the medical issue, this software is a great example to simulate automation in the healthcare industry. Since the priority queue only cares about the values, no matter what value you put in based on ANY medical issue, the priority queue will always output the patients based on their medical issues. 


# How the software rates medical issues
Based on any *natural* number. For the software to output a proper list of patients based on medical issues, the user themselves must evaluate the medical issue ranging from any natural number. The ratings must be reasonable (for ex, `heart attack: 4` and `headache: 2`), otherwise, the software may output a queue that might have the order messed up.

- `The higher the rating` = The More Dangerous 
- `The lower the rating` = Less Serious 



# Extras

Typing must be accurate in this software. For example, `"Headache"` must be written as `"Headache"` and not `"headache"`, otherwise the software will through an error.

*Controls* are going to be listed when the software is launched for both the `user database` and `patient database`. 

To fully quit the software, you may need to type `/quit` twice one-by-one (*This will mostly happen when you are in the patient database*).

If the hopsital name does not show up in the user database, that means the program has overriden another hospital object that may have the same hash_code. Therefore, you may need to re-write the new hospital in a different way (for ex, include numbers, characters, capitals, etc.)

Made in Python 🐍
