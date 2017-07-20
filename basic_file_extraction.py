import re
def parameter_extraction():
    print ("Hii")
    f=open('/home/sagar/Desktop/install_dir/diag-insights-rules/diag_insights_rules/kernel/plugins/localhost_in_hosts.py','r') 
    strings=re.findall(r'ERROR_KEY = ([\"\'\w\s]+)', f.read())

    for var1 in strings:
        print var1

parameter_extraction()
