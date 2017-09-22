import requests
import json

def GetEvaluation( course ):
    req = requests.get('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees')
    req_json = json.loads(req.text)
    for entry in req_json:
        if entry["acronym"] == course:
            couse_id = entry["id"]
            ep_courses = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees/" + couse_id + "/courses"
            req_courses = requests.get(ep_courses)
            courses = json.loads(req_courses.text)
            eval_list = dict()
            days = []
            for course in courses:
                ep_eval = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/courses/" + course["id"] + "/evaluations"
                req_eval = requests.get(ep_eval)
                evaluations = json.loads(req_eval.text)
                for evaluation in evaluations:
                    if evaluation["type"] == "TEST" or evaluation["type"] == "EXAM":
                        per = evaluation["evaluationPeriod"]
                        day = per["start"][0:10]
                        if day not in days:
                            days.append(day)
                            l = []
                            l.append(per)
                            eval_list[day] = l
                        else:
                            l.append(per)
                            eval_list[day]= l

            return eval_list

evaluations = GetEvaluation("MEEC")
print(evaluations)
