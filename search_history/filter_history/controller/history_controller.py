from filter_history.models import User, Keyword, Result, History
import json

def get_history():
    users = User.objects.all()
    keywords = Keyword.objects.all()
    search_details = {}
    for keyword in keywords:
        search_details[keyword.word] = {}
        histories = History.objects.filter(keyword=keyword)
        search_details[keyword.word]['user'] = []
        for history in histories:
            search_details[keyword.word]['user'].append([history.user.id, str(history.date)])
            results = Result.objects.filter(keyword=keyword)
            search_details[keyword.word]['result'] = []
            for result in results:
                search_details[keyword.word]['result'].append(result.search_result)
    context = {
        'users': users,
        'keywords': keywords,
        'loop': range(20),
        'search_details': json.dumps(search_details)
    }
    return context;