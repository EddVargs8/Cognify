from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Criminal, Memory
from .forms import CriminalForm, MemoryForm

def home(request):
    criminals = Criminal.objects.all() 
    return render(request, 'home.html', {'criminals': criminals})

def add_criminal(request):
    if request.method == 'POST':
        form = CriminalForm(request.POST)
        if form.is_valid():
            criminal = form.save()
            if criminal.sentence_type == 'cognify':
                return redirect('personalize_memory', criminal_id=criminal.id)
            else:
                return redirect('home')
    else:
        form = CriminalForm()
    return render(request, 'add_criminal.html', {'form': form})

def personalize_memory(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)

    # Define opciones de recuerdos basados en el tipo de crimen
    if criminal.crime_type == 'violent':
        memory_options = [
            "Vivir el sufrimiento de la víctima desde su perspectiva en el momento del crimen: una experiencia de angustia, miedo y vulnerabilidad total. Sentir el pánico, el dolor y la impotencia mientras el crimen ocurre, experimentando la sensación de pérdida de control sobre su propio cuerpo y mente.",
            "Ser testigo del sufrimiento y la desesperación de los familiares de la víctima. Observar cómo el crimen afecta a sus seres queridos: los hijos, padres y amigos enfrentando el duelo, la tristeza y el vacío dejado por la pérdida. Sentir la tristeza de una vida rota y las cicatrices emocionales que perduran en sus vidas.",
            "Experimentar el rechazo y la desconfianza de la comunidad hacia uno mismo tras el crimen. Sentir el aislamiento y la mirada crítica de la sociedad, percibiendo la culpa y la vergüenza constantes que siguen a una acción violenta, y cómo esas acciones impactan en el bienestar colectivo y la cohesión social."
        ]
    elif criminal.crime_type == 'financial':
        memory_options = [
            "Sentir el impacto de la pérdida financiera en la vida cotidiana de las víctimas, viendo a una familia perder sus ahorros de años y enfrentarse a dificultades económicas. Vivir la desesperación de las personas al ver comprometido su futuro financiero, la educación de sus hijos y la estabilidad de su hogar por culpa de una estafa.",
            "Experimentar el dolor y la vergüenza de quienes fueron engañados y han perdido no solo dinero, sino también su credibilidad y reputación. Vivir la humillación pública de la pérdida, y el impacto en sus relaciones personales y laborales debido a la falta de confianza en sí mismos y en otros.",
            "Percibir cómo las acciones fraudulentas destruyen la confianza en la comunidad. Sentir la desconfianza que afecta al entorno de trabajo, negocios y relaciones familiares de las víctimas. Experimentar el daño que un solo acto de fraude puede causar, deteriorando la cohesión social y afectando la economía local."
        ]
    elif criminal.crime_type == 'hate':
        memory_options = [
            "Experimentar la vida de una persona que es constantemente juzgada y rechazada por sus características personales, como su raza, religión o identidad. Sentir la constante opresión y el miedo al rechazo, viviendo el dolor de no ser aceptado y de enfrentar prejuicios diarios.",
            "Vivir el aislamiento y la soledad de una persona que ha sido marginada por su identidad. Experimentar cómo el odio y la intolerancia afectan el bienestar emocional y psicológico, enfrentando la tristeza de ser excluido de su propia comunidad y la dificultad de encontrar apoyo.",
            "Sentir la riqueza y valor de la diversidad en una sociedad que abraza las diferencias. Percibir la conexión emocional con personas de diferentes trasfondos y el impacto positivo de una comunidad inclusiva. Vivir la gratitud y el respeto hacia quienes promueven la comprensión, creando empatía y respeto profundo."
        ]

    if request.method == 'POST':
        form = MemoryForm(request.POST)
        return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'personalize_memory.html', {
        'form': form,
        'criminal': criminal,
        'memory_options': memory_options
    })

def simulation_result(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)
    memory = Memory.objects.filter(criminal=criminal).first()
    return render(request, 'simulation_result.html', {'criminal': criminal, 'memory': memory})
