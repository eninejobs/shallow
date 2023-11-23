from django.views.generic import TemplateView
# from qux.seo.mixin import SEOMixin


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {
        "roles": [
            {
                "name": "Senior Developer"
            },
            {
                "name": "Developer"
            },
            {
                "name": "Intern"
            },
            {
                "name": "Summer Intern"
            }
        ],
        "responsibilities": [
            {
                "name": "Develop applications"
            },
            {
                "name": "Write tests"
            },
            {
                "name": "Write documentation"
            },
            {
                "name": "Deploy applications"
            }
        ],
        "requirements": [
            {
                "name": "Minimum",
                "items": [
                    "Excellent communication skills",
                    "Strong analytical skills",
                    "Obsessed with details",
                    "Programming experience",
                    "Experience with one or more general purpose languages",
                    "Expertise in python 3.7+"
                ]
            },
            {
                "name": "Preferred",
                "items": [
                    "Linux",
                    "Shell scripting",
                    "Git (github and/or bitbucket)",
                    "Django",
                    "Flask",
                    "Javascript",
                    "HTML5/CSS",
                    "Bootstrap",
                ]
            },
            {
                "name": "Extra",
                "items": [
                    "Numpy",
                    "Pandas",
                    "D3",
                    "Solved Project Euler (<a href='https://projecteuler.net/'>projecteuler.net</a>) problems",
                ]
            }
        ]
    }


class ApplyView(TemplateView):
    template_name = 'apply.html'
