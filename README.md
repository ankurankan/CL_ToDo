Command Line ToDo list manager
=======


<pre>
Add: add a task 
	options:d: Specify a date
		t: specify a time



Get: see tasks
	options:d: Specify the date of the tasks
		re: regular expression search of tasks
		x: exact search of tasks
		use a language to filter out *


complete: mark a task as complete. One/more than one tasks can be marked and can be
 selected through these options.
	options:d:Specify the date of the tasks
		re: Search by a regular expression
		x: exact search of tasks



remove: removes a task from the list.
	options:d:Date of the task: Returns a list of tasks on that date
		re: Search by a regular expression
		x: exact search of tasks



modify: modify tasks. Selecting the task based on the following options:
	options:d:returns all the tasks of that date
		re: Search by a regular expression. If date had been specified searches within
            the tasks of that date
		x: Searches for exact tasks. If date specified searches within the tasks 
            of that date



To add: *A laguage for better searching of tasks as in mercurial.



Always be asked for conformation with all the tasks returned by the search with the 
option which one to mark.

Features to be added in the language:
	Providing the feature of specifying range of date or time.
</pre>
