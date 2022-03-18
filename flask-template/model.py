# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/results', methods = ['POST'])

def answers(answer):



    correct_answers = {'ID': 'Boise', 'NY': 'Albany', 'CA': 'Sacramento', 'TX': 'Austin', 'IL': 'Springfield'}
    output = {}

    for el in answer:

        if answer[el] == '':

            return ''

        if answer[el].lower() == correct_answers[el].lower():
            output[el] = el + ': ' + correct_answers[el] + ' is correct!'

        else:
            output[el] = el + ':' + answer[el] + ' is incorrect. It should be ' + correct_answers[el] + '!'

    return output       



