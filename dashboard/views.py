from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import *
from django.views.generic import TemplateView


# Create your views here.

def home(request):
    return render(request, 'index_dash.html')


def login_dash(request):
    return render(request, 'login_dash.html')


def tables_dash(request):
    table = Staging.objects.all()
    return render(request, 'tables.html', {'table': table})


def utilities_animation(request):
    return render(request, 'utilities-animation.html')


def utilities_border(request):
    return render(request, 'utilities-border.html')


def utilities_color(request):
    return render(request, 'utilities-color.html')


def utilities_other(request):
    return render(request, 'utilities-other.html')


def error_404(request):
    return render(request, '404.html')


def blank_dash(request):
    return render(request, 'blank.html')


def buttons_dash(request):
    return render(request, 'buttons.html')


def cards_dash(request):
    return render(request, 'cards.html')


def charts_dash(request):
    return render(request, 'charts.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return redirect('/choose')


def badrecords_dash(request):
    return(request,'badrecords_dash.html')


def manageteam_dash(request):
    return(request,'manageteam_dash.html')

def display_mandate(request):
    return(request,'display_mandate.html')

def upload_candidate(request):
    return(request,'upload_candidate.html')

def display_candidate(request):
    return(request,'display_candidate.html')

def mandate_upload(request): 
    return redirect('/mandate_choose')

def upload_mandate(request):
    return redirect('/mandate_choose')


class BarChartview(TemplateView):
    template_name = 'bar_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Staging.objects.all()
        return context


'''def mandate_choose(request):
    if request.method == 'POST':
        if request.POST.get('checkBox') == None:
            return redirect('/mandate_import')

        return redirect('/mandate_import_p')
    else:
        return render(request, 'mandate-choose.html')


@csrf_exempt
def mandate_import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/mandate_fieldmatching?df=' + path_name)
    else:
        return render(request, 'mandate-import_data.html')

def mandate_fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Mandates._meta.get_fields()]
        df = df.transform(lambda x: x.fillna('TNone') if x.dtype == 'object' else x.fillna(0))
        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in fields}
            x = list(matched.keys())
            y = list(matched.values())
            dict = {}
            for key in y:
                for value in x:
                    dict[key] = value
                    print(dict)
                    x.remove(value)
                    break
            df.rename(columns=dict, inplace=True)


        dictionary = df.to_dict(orient="index")
        Mapping.objects.create(MappingFor='Mandates', Mappings=dict)
        print(Mapping.objects.all()[0].Mappings)
        mandate_save_dict(dictionary)
        return render(request, 'mandate-import_data.html')
    else:
            path_name = request.GET.get('df')
            df = pd.read_csv(path_name)
            names = list(df.columns)
            fields = [field.name for field in Mandates._meta.get_fields()]
    
            
            return render(request, 'mandate-fieldmatching.html',
                      {'fields': fields, 'path_name': path_name, 'names': names})

def mandate_save_dict(dictionary):
    for index, object in dictionary.items():
        m = Mandates()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', index)
        m.save()


def mandate_save_dict_call(dictionary, q):
    for index, object in dictionary.items():
        m = Mandates()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', q)
        q = q + 1;
        m.save()


def mandate_import_data_p(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        df = pd.read_csv(path_name)
        df = df.transform(lambda x: x.fillna('None') if x.dtype == 'object' else x.fillna(0))
        # declare store dictionary i.e we want dict
        p = Mapping.objects.order_by('-id').filter(MappingFor = 'Mandates')[0].Mappings
        print(p)
        dict = {}
        #print(dict)
        if not bool(p):
            print("No Previous Matching Columns Found")
            return redirect('/mandate_choose')
        else:
            df.rename(columns=p, inplace=True)
            engine = create_engine('postgresql://postgres:willoffire@1@localhost:5432/Candidate')
            #df.to_sql(name='Mandate', con=engine, if_exists='append', index=False)
            q = Mandates.objects.count()
            print(q)
            #q = q + 1
            # df.set_index('id', drop=True, inplace=True)
            dictionary = df.to_dict(orient="index")
            mandate_save_dict_call(dictionary, q)
            print("columns found")
        # save_dict(dictionary)
        return render(request, 'mandate-import_data.html')
    else:
        q = Mapping.objects.order_by('-id').filter(MappingFor = 'Staging')[0].Mappings
        print(q)
        p = Mapping.objects.order_by('-id').filter(MappingFor = 'Mandates')[0].Mappings
        print(p)
        return render(request, 'mandate-import_data.html')'''


