//Übungen Klassen
const exercises = {

    back: [
        "Klimmzüge",
        "Latzug",
        "Rudern",
        "Enges Rudern"
    ],

    chest: [
        "Bankdrücken",
        "Bankdrücken schräg",
        "Butterfly",
        "Schrägbankdrücken",
        "Brustpresse"
    ],

    arms: [
        "Bizeps curls Z Stange",
        "Bizeps curls Kurzhantel",
        "Bizeps curls 45°",
        "Hammer curls ",
        "Trizepsdrücken",
        "Skull crusher"
    ],

    shoulder: [
        "Seitheben",
        "Schulterpresse"
    ],

    legs: [
        "Squats",
        "Bulgarische Split Squats",
        "Beinpresse",
        "Kreuzheben"
    ]

};

function fillExerciseSelect(selectId, exerciseList)
{

    const select = document.getElementById(selectId);
    for (const exerciseName of exerciseList)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }
}
fillExerciseSelect("backExercise1", exercises.back);
fillExerciseSelect("chestExercise1", exercises.chest);
fillExerciseSelect("armExercise1", exercises.arms);
fillExerciseSelect("shoulderExercise1", exercises.shoulder);
fillExerciseSelect("legExercise1", exercises.legs);

//-------------------------------------------create_workout.html-------------------------------------------
function addBackExercise()
{
    const backExercises = document.getElementById("backExercises");
    const exerciseCount = backExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "backExercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "backExercise" + (exerciseCount + 1);
    select.name = "backExercise" + (exerciseCount + 1);

    for (const exerciseName of exercises.back)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }

    exercise.appendChild(label);
    exercise.appendChild(select);
    backExercises.appendChild(exercise);
}

function addChestExercise()
{
    const chestExercises = document.getElementById("chestExercises");
    const exerciseCount = chestExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "chestExercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "chestExercise" + (exerciseCount + 1);
    select.name = "chestExercise" + (exerciseCount + 1);

    for (const exerciseName of exercises.chest)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }

    exercise.appendChild(label);
    exercise.appendChild(select);
    chestExercises.appendChild(exercise);
}

function addArmsExercise()
{
    const armsExercises = document.getElementById("armsExercises");
    const exerciseCount = armsExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "armsExercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "armsExercise" + (exerciseCount + 1);
    select.name = "armsExercise" + (exerciseCount + 1);

    for (const exerciseName of exercises.arms)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }

    exercise.appendChild(label);
    exercise.appendChild(select);
    armsExercises.appendChild(exercise);
}

function addShoulderExercise()
{
    const shoulderExercises = document.getElementById("shoulderExercises");
    const exerciseCount = shoulderExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "shoulderExercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "shoulderExercise" + (exerciseCount + 1);
    select.name = "shoulderExercise" + (exerciseCount + 1);

    for (const exerciseName of exercises.shoulder)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }

    exercise.appendChild(label);
    exercise.appendChild(select);
    shoulderExercises.appendChild(exercise);
}

function addLegsExercise()
{
    const legsExercises = document.getElementById("legsExercises");
    const exerciseCount = legsExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "legsExercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "legsExercise" + (exerciseCount + 1);
    select.name = "legsExercise" + (exerciseCount + 1);

    for (const exerciseName of exercises.legs)
    {
        const option = document.createElement("option");

        option.textContent = exerciseName;
        option.value = exerciseName;
        select.appendChild(option);
    }

    exercise.appendChild(label);
    exercise.appendChild(select);
    legsExercises.appendChild(exercise);
}