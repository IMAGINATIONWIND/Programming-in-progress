import re

##used to find a specific pattern in a large group of text fairly easily , efficiently
pattern = "the"
text = '''There are some goals that you may only be able to accomplish during business hours, or
some that you can only do on Saturday when your children are home. Can you begin to see some
of the advantages of organizing the week instead of the day?
Having identified roles and set goals, you can translate each goal to a specific day of the
week, either as a priority item or, even better, as a specific appointment. You can also check your
annual or monthly calendar for any appointments you may have previously made and evaluate
their  importance  in  the  context  of  your  goals,  transferr'''

# matches = re.search(pattern,text)
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])