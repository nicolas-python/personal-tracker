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

    //Sätze Rücken
    const setsLabel = document.createElement("label");
    setsLabel.textContent = "Sätze:";
    setsLabel.htmlFor = "backSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "backSets" + (exerciseCount + 1);
    setsInput.name = "backSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Rücken
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "backReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "backReps" + (exerciseCount + 1);
    repsInput.name = "backReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Rücken
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "backWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "backWeight" + (exerciseCount + 1);
    weightInput.name = "backWeight" + (exerciseCount + 1);
    weightInput.min = "0";
    weightInput.step = "0.5";

    exercise.appendChild(label);
    exercise.appendChild(select);

    exercise.appendChild(setsLabel);
    exercise.appendChild(setsInput);

    exercise.appendChild(repsLabel);
    exercise.appendChild(repsInput);

    exercise.appendChild(weightLabel);
    exercise.appendChild(weightInput);

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

    //Sätze Brust
    const setsLabel = document.createElement("label");
    setsLabel.textContent = "Sätze:";
    setsLabel.htmlFor = "chestSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "chestSets" + (exerciseCount + 1);
    setsInput.name = "chestSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Brust
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "chestReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "chestReps" + (exerciseCount + 1);
    repsInput.name = "chestReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Brust
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "chestWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "chestWeight" + (exerciseCount + 1);
    weightInput.name = "chestWeight" + (exerciseCount + 1);
    weightInput.min = "0";
    weightInput.step = "0.5";

    exercise.appendChild(label);
    exercise.appendChild(select);

    exercise.appendChild(setsLabel);
    exercise.appendChild(setsInput);

    exercise.appendChild(repsLabel);
    exercise.appendChild(repsInput);

    exercise.appendChild(weightLabel);
    exercise.appendChild(weightInput);

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

    //Sätze Arme
    const setsLabel = document.createElement("label");
    setsLabel.textContent = "Sätze:";
    setsLabel.htmlFor = "armSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "armSets" + (exerciseCount + 1);
    setsInput.name = "armSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Arme
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "armReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "armReps" + (exerciseCount + 1);
    repsInput.name = "armReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Arme
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "armWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "armWeight" + (exerciseCount + 1);
    weightInput.name = "armWeight" + (exerciseCount + 1);
    weightInput.min = "0";
    weightInput.step = "0.5";

    exercise.appendChild(label);
    exercise.appendChild(select);

    exercise.appendChild(setsLabel);
    exercise.appendChild(setsInput);

    exercise.appendChild(repsLabel);
    exercise.appendChild(repsInput);

    exercise.appendChild(weightLabel);
    exercise.appendChild(weightInput);

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

    //Sätze Schultern
    const setsLabel = document.createElement("label");
    setsLabel.textContent = "Sätze:";
    setsLabel.htmlFor = "shoulderSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "shoulderSets" + (exerciseCount + 1);
    setsInput.name = "shoulderSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Schultern
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "shoulderReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "shoulderReps" + (exerciseCount + 1);
    repsInput.name = "shoulderReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Schultern
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "shoulderWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "shoulderWeight" + (exerciseCount + 1);
    weightInput.name = "shoulderWeight" + (exerciseCount + 1);
    weightInput.min = "0";
    weightInput.step = "0.5";

    exercise.appendChild(label);
    exercise.appendChild(select);

    exercise.appendChild(setsLabel);
    exercise.appendChild(setsInput);

    exercise.appendChild(repsLabel);
    exercise.appendChild(repsInput);

    exercise.appendChild(weightLabel);
    exercise.appendChild(weightInput);

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

    //Sätze Beine
    const setsLabel = document.createElement("label");
    setsLabel.textContent = "Sätze:";
    setsLabel.htmlFor = "legSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "legSets" + (exerciseCount + 1);
    setsInput.name = "legSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Beine
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "legReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "legReps" + (exerciseCount + 1);
    repsInput.name = "legReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Beine
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "legWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "legWeight" + (exerciseCount + 1);
    weightInput.name = "legWeight" + (exerciseCount + 1);
    weightInput.min = "0";
    weightInput.step = "0.5";


    exercise.appendChild(label);
    exercise.appendChild(select);

    exercise.appendChild(setsLabel);
    exercise.appendChild(setsInput);

    exercise.appendChild(repsLabel);
    exercise.appendChild(repsInput);

    exercise.appendChild(weightLabel);
    exercise.appendChild(weightInput);

    legsExercises.appendChild(exercise);
}