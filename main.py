
# library modules
from jira import JIRA

user = 'a.nemchenko@omnidata.ru'
apikey = 'Ii9JaTGq0PSBSyMGqaPbDD42'
server = 'https://data4retail.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

#ticket = 'SRMDEV-210'
#issue = jira.issue(ticket)

#summary = issue.fields.summary
#time_1 = issue.fields.worklog.worklogs[1].timeSpent

#print('ticket: ', ticket, summary, time_1)

# print all of the project keys as an example
#for project in jira.projects():
#    print(project.key, project.name)

#issue_n = jira.issue('SRMDEV-210', fields='summary,comment, description')
#print(issue_n)


# Search returns first 50 results, `maxResults` must be set to exceed this
issues_in_proj = jira.search_issues('project=SRMDEV')
all_proj_issues_but_mine = jira.search_issues('project=SRMDEV')

# my top 5 issues due by the end of the week, ordered by priority
#oh_crap = jira.search_issues('assignee = currentUser() and due < endOfWeek() order by priority desc', maxResults=5)


issue = jira.issue('SRMDEV-83', fields='summary,comment')
print(issue)


# Summaries of my last 3 reported issues
for issue in jira.search_issues('project=SRMDEV and status = Done', maxResults=2):
    print('{}: {}: {} : {}, {}'.format(issue.key, issue.fields.summary, issue.fields.status, issue.fields.created, issue.fields.labels))



issue2 = jira.issue('SRMDEV-83')
print(issue2.fields.project.key)            # 'JRA'
print(issue2.fields.issuetype.name)         # 'New Feature'
print(issue2.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'