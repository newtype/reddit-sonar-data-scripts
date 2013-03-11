import praw

user_agent = "Find Subreddits Test by u/newtype0087"
r = praw.Reddit(user_agent=user_agent)

user_name = "speedracer111"
user = r.get_redditor(user_name)
thing_limit = 25

comments_gen = user.get_comments(limit=thing_limit)
comment_subreddits = set()
for thing in comments_gen:
    comment_subreddits.add(thing.subreddit.title)

print "[COMMENTS]"
for subreddit in sorted(comment_subreddits):
    print subreddit

submitted_gen = user.get_submitted(limit=thing_limit)
submitted_subreddits = set()
for thing in submitted_gen:
    submitted_subreddits.add(thing.subreddit.title)
    
print "[SUBMITTED]"
for subreddit in sorted(submitted_subreddits):
    print subreddit

# TODO use counter to count subreddits and sort by Counter.most_common
