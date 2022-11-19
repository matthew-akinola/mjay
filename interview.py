twitter_api = [
    {
        "name": "Matthew",
        "age": 42,
        "followers": 400000,
        "vip_score": 1
    }, {
        "name": "Matthew",
        "age": 50,
        "followers": 7000000,
        "vip_score": 3
    }, {
        "name": "Matthew",
        "age": 25,
        "followers": 600000,
        "vip_score": 2
    }, {
        "name": "Matthew",
        "age": 18,
        "followers": 950000,
        "vip_score": 2
    },{
        "name": "Matthew",
        "age": 20,
        "followers": 20000,
        "vip_score": 2
    },{
        "name": "Matthew",
        "age": 20,
        "followers": 207500,
        "vip_score": 2
    }, {
        "name": "Matthew",
        "age": 34,
        "followers": 200000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 200000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 2000000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 43,
        "followers": 2000000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 27,
        "followers": 750000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 36,
        "followers": 370000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 60,
        "followers": 650000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 53,
        "followers": 740000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 40,
        "followers": 930000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 1000000,
        "vip_score": 3
    },
     {
        "name": "Matthew",
        "age": 32,
        "followers": 730000,
        "vip_score": 2
    },
]



facebook_api = [
    {
        "name": "Matthew",
        "age": 40,
        "followers": 400000,
        "vip_score": 1
    }, {
        "name": "Matthew",
        "age": 50,
        "followers": 7000000,
        "vip_score": 3,
        "email": "matthew@gmail.com"
    }, {
        "name": "Matthew",
        "age": 25,
        "followers": 600000,
        "vip_score": 1
    }, {
        "name": "Matthew",
        "age": 18,
        "followers": 950000,
        "vip_score": 2,
        "email": "mattheuw@gmail.com"
    }
]




celebrity_api = [
    {
        "name": "Matthew",
        "age": 49,
        "followers": 400000,
        "vip_score": 1,
        "email": "matthew@gmail.com"
    }, 
    {
        "name": "Matthew",
        "age": 50,
        "followers": 7000000,
        "vip_score": 3,
        "email": "matthew2@gmail.com"
    }, 
    {
        "name": "Matthew",
        "age": 25,
        "followers": 600000,
        "vip_score": 2,
        "email": "mathew@gmail.com"
    }, {
        "name": "Matthew",
        "age": 18,
        "followers": 950000,
        "vip_score": 2
    },{
        "name": "Matthew",
        "age": 20,
        "followers": 20000,
        "vip_score": 2
    },{
        "name": "Matthew",
        "age": 20,
        "followers": 207500,
        "vip_score": 2
    }, {
        "name": "Matthew",
        "age": 34,
        "followers": 200000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 200000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 2000000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 43,
        "followers": 2000000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 27,
        "followers": 750000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 36,
        "followers": 370000,
        "vip_score": 1
    },
     {
        "name": "Matthew",
        "age": 60,
        "followers": 650000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 53,
        "followers": 740000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 40,
        "followers": 930000,
        "vip_score": 2
    },
     {
        "name": "Matthew",
        "age": 20,
        "followers": 1000000,
        "vip_score": 3
    },
     {
        "name": "Matthew",
        "age": 32,
        "followers": 730000,
        "vip_score": 2
    },
]



from operator import itemgetter


def vip_score_calc(**kwargs):
    a = zip(twitter_api,facebook_api,celebrity_api)
    # print(a)
    # for (a,b,c) in zip(twitter_api, facebook_api, celebrity_api):
    result = []
    vip_score_total = 0
    # sort the list of consumed apis based on number of followers in a descending order
    # since if the disctinct user is a celebrity, he should have the highest follower across
    # two or more platforms
    twitter = sorted(twitter_api, key=itemgetter('followers'), reverse=True)
    facebook = sorted(facebook_api, key=itemgetter('followers'), reverse=True)
    linkedin = sorted(celebrity_api, key=itemgetter('followers'), reverse=True)
    # check if the age of the person across 2 or more searched platforms is the same
    if twitter[0]['age'] == facebook[0]['age'] or linkedin[0]['age']:
        # if the age of the user  with the highest follower is the same 
        # across 2 or more platforms, add the user to the result list
        result.extend([twitter[0], facebook[0], linkedin[0]])
        for vip_score in result:
            vip_score_total += vip_score['vip_score']
        # the final vip score is the average  of the user's vip score across
        # searched platforms
        average_vip_score = int(vip_score_total / len(result))
        user_profile = {
            "name": result[0]['name'],
            "age": result[0]['age'],
            "vip_score": average_vip_score
        }
        # print(user_profile)


vip_score_calc()








# # def multipliers(): 
# #     return [lambda x : i * x for i in range(4)] 

# # print ([m(2) for m in multipliers()])




# a = {"name":"apple", "age":20, "vip_score": 3}
# b = {"name":"apple", "age":20, "vip_score": 2}
# c = {"name":"apple", "age":20, "vip_score": 1}
# d = {"name":"apple", "age":20, "vip_score": 2}
# e = {"name":"apple", "age":20, "vip_score": 3}
# # e = {"google", "microsoft", "apple"}

# z = a.intersection(b,c,d,e)

# print(z)