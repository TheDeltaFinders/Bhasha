import datetime

from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from django.template import RequestContext
from django.template import loader

from .models import BaseWord
from .models import Pos
from .models import SubWord
from .models import Meaning


from .forms import CommentForm


class WordInfo():
    def __init__(self,word_obj,sub=False):
        self.word = word_obj.word if not sub else word_obj.parentword.word+word_obj.subword
        self.meaning = [(mean.pos.partname,mean.meaning) for mean in word_obj.meaning.all()]

class KoshIndex(View):
    def get(self,request):
        #allposts = BlogPost.objects.all()
        template = loader.get_template('kosh/index.html')
        allbwords = BaseWord.objects.all()
        allswords = SubWord.objects.all()

        base_view_word_list = [WordInfo(wordobj) for wordobj in allbwords]
        sub_view_word_list = [WordInfo(wordobj,True) for wordobj in allswords]
        allwords = base_view_word_list + sub_view_word_list 


        context = {
            'allwords': allwords
        }
        return HttpResponse(template.render(context,request))


class WordMeaning(View):
    def get(self,request,pslug=None):
        template = loader.get_template('kosh/meaning.html')
        word = None
        try:
            word = BaseWord.objects.filter(word=pslug)[0]
        except:
            template = loader.get_template('404.html')

            # 3. Return Template for this view + Data
            return HttpResponse(content=template.render({}), content_type='text/html; charset=utf-8', status=404)

        print(f'word obtained is {word} whereas pslug was {pslug}')
        form = CommentForm()
        context = {
            'word': WordInfo(word),
            'form':form
        }
        
        return HttpResponse(template.render(context,request))

    def post(self,request,**kwargs):
        return HttpResponseRedirect('kosh/index.html')

    
class BlogDownload(View):
    def get(self,request):
        template = loader.get_template('kosh/download.html')
        context = {}
        return HttpResponse(template.render(context,request))

def handler404(request,*args):
    response = render_to_response('404.html',{},context_instance=RequestContext(request))
    response.status_code = 404
    return response

