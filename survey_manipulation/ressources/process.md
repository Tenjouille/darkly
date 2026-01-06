# The SURVEY Page

This page allows you to grade (from 1 to 10) different subjects, in a 4 columns table :
1. The first column is an input field for you to grade a subject
2. The second column gives you the average score of the given subject
3. The name of the current subject
4. The total number of vote for this subject.

## Wait, something's wrong

Indeed, you can see that the *Average* value for thge subject *wil* equals to 4218.19, where it should be the average of 1 to 10 grades (so between 1 and 10).

## How is it possible ?

Two options possible : 
* The administrator alter the votes in his favors
* There is a breach allowing you to give a note bigger than 10.

While waiting for the admin to answer our phone calls, we can inspect the breach lead.

## The Breach

By inspecting with the DevTool the survey page, more precisely the input tags, you can see that the form which submit your grade contain a select tag with option tags going from 1 to 10. This structure allows devs to easily create a drop-down list, but allows you to modify in devTool the options properties *value* which will be sent in the form submit.

## Mitigation

If you use a select -> option tag combination, you need to check the submitted value before using it. In this exemple : 

`if value <= 0 or value > 10: return false`