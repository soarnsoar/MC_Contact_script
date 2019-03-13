from html_maker import *
a=jh_html()
a.title="test title"
a.tabs=["1st","2nd","3rd"]

a.add_data(["a","b","c"])
a.make()
