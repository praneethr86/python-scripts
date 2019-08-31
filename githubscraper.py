from github import Github
from datetime import datetime, timedelta

g = Github(base_url="https://github.com/api/v3", login_or_token="<token>")

repolist = ["repo1", "repo2"]

def main():
	for repoName in repolist:
		repo = g.get_repo(repoName)
		pulls = repo.get_pulls(state='closed', sort='created', direction='desc', base='develop')
		print('\n\nRepo: ' + repoName)
		for pr in pulls:
			returnvalue = printPRResults(pr)
			if(not returnvalue): 
				break


def printPRResults(pr):
	if (pr.created_at > (datetime.now() - timedelta(days=2))):
		print('\nTitle: ' + pr.title )
		print('PR: ' + pr.html_url)
		print('User: ' + pr.user.login + '\tcreated_at: '+ str(pr.created_at))
		return True;
	else:
		return False;

main()

