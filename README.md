cs373-collatz
=============

Collatz: Project 1 for CS 373 Software Engineering

The Collatz conjecture is a conjecture in mathematics named after Lothar Collatz, who first proposed it in 1937. Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO) indefinitely. The conjecture is that no matter what number you start with, you will always eventually reach 1. The property has also been called oneness.

    1)	Estimate time to completion.
    2)	Get an educational account with 5 private repos at GitHub.
    3)	Create a private Git repository at GitHub, named cs373-collatz.
    4)	Add these requirements to the issue tracker at GitHub, at least 10 issues.
    	Add at least 10 more issues, one for each bug or feature, both open and closed with a good description and a label.
    5)	Invite the grader to your private code repo.
    6)	Confirm that the grader has invited you back to the public test repo.
    7)	Clone your private code repo onto your local directory.
    8)	Make at least 5 commits, one for each bug or feature.
    	If you cannot describe your changes in a sentence, you are not committing often enough.
    	Make meaningful commit messages identifying the corresponding issue in the issue tracker (see here).
    9)	Clone the public class repo onto your local directory.
    	It is critical that you clone the public class repo into a different directory than the one you're using for your private code repo.
    10)	Copy the code files from the clone of the public class repo to the clone of the private 	code repo.
    11)	Run RunCollatz.py and TestCollatz.py, confirm the expected failures, and add, commit, 		and push to the private code repo.
    12)	Write more unit tests in TestCollatz.py that test corner cases and failure cases until 		you have an average of 3 tests for each function, confirm the expected failures, and 		add, commit, and push to the private code repo.
    13)	Implement and debug the simplest possible solution in collatz_eval() in Collatz.py with 	assertions that check pre-conditions, post-conditions, argument validity, and return-		value validity, until all tests pass, and add, commit, and push to the private code repo.
    14)	Combine Collatz.py and RunCollatz.py into SphereCollatz.py (don't forget to remove 			import).
    15)	Create an account on Sphere.
    16)	Submit SphereCollatz.py to Sphere and confirm the likely result of time exceeded or 		wrong answer.
    17)	Debug the code until it's accepted by Sphere, and add, commit, and push to the private 		code repo.
    18)	Create 1000 lines of acceptance tests in RunCollatz.in and RunCollatz.out that test 		corner cases and failure cases, and add, commit, and push to the private code repo.
    19)	Clone the public test repo onto your local directory.
    	It is critical that you clone the public test repo into a different directory than the one you're using for your private code repo.
    20)	Copy your unit tests and your acceptance tests to your clone of the public test repo, 		rename the files, do a git pull to synchronize your clone, and then add, commit and push 	 to the public test repo.
    	The files MUST be named <cs-username>-RunCollatz.in, <cs-username>-RunCollatz.out, <cs-username>-TestCollatz.py, and <cs-username>-TestCollatz.out in the public test repo.
    21)	Implement and debug the simplest possible cache until all tests pass, and add, commit, 		and push to the private code repo.
    22)	Submit and debug until accepted by Sphere and add, commit, and push to the private code 	repo.
    23)	Run pydoc on Collatz.py, which will create Collatz.html, that then documents the 			interfaces to your functions.
    24)	Create inline comments if you need to explain the why of a particular implementation.
    	Use a consistent coding convention with good variable names, good indentation, blank lines, and blank spaces.
    	Create a log of your commits in Collatz.log.
    25) Obtain the git SHA with git rev-parse HEAD
    26)	Fill in the Google Form.
    27)	It is your responsibility to protect your code from the rest of the students in the 		class. If your code gets out, you are as guilty as the recipient of academic dishonesty.
