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
//-------------------------------------------create_workout.html-------------------------------------------
function addBackExercise()
{
    const backExercises = document.getElementById("backExercises");
    const exerciseCount = backExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";
    const deleteButton = createDeleteButton(exercise);

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

    exercise.appendChild(deleteButton);
    backExercises.insertBefore(exercise, backExercises.querySelector(".addExercise"));
}


function addChestExercise()
{
    const chestExercises = document.getElementById("chestExercises");
    const exerciseCount = chestExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";
    const deleteButton = createDeleteButton(exercise);

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

    exercise.appendChild(deleteButton);
    chestExercises.insertBefore(exercise, chestExercises.querySelector(".addExercise"));
}

function addArmsExercise()
{
    const armsExercises = document.getElementById("armsExercises");
    const exerciseCount = armsExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";
    const deleteButton = createDeleteButton(exercise);

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
    setsLabel.htmlFor = "armsSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "armsSets" + (exerciseCount + 1);
    setsInput.name = "armsSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Arme
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "armsReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "armsReps" + (exerciseCount + 1);
    repsInput.name = "armsReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Arme
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "armsWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "armsWeight" + (exerciseCount + 1);
    weightInput.name = "armsWeight" + (exerciseCount + 1);
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

    exercise.appendChild(deleteButton);
    armsExercises.insertBefore(exercise, armsExercises.querySelector(".addExercise"));
}

function addShoulderExercise()
{
    const shoulderExercises = document.getElementById("shoulderExercises");
    const exerciseCount = shoulderExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";
    const deleteButton = createDeleteButton(exercise);

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

    exercise.appendChild(deleteButton);
    shoulderExercises.insertBefore(exercise, shoulderExercises.querySelector(".addExercise"));
}

function addLegsExercise()
{
    const legsExercises = document.getElementById("legsExercises");
    const exerciseCount = legsExercises.querySelectorAll(".exercise").length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";
    const deleteButton = createDeleteButton(exercise);

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
    setsLabel.htmlFor = "legsSets" + (exerciseCount + 1);

    const setsInput = document.createElement("input");
    setsInput.type = "number";
    setsInput.id = "legsSets" + (exerciseCount + 1);
    setsInput.name = "legsSets" + (exerciseCount + 1);
    setsInput.min = "1";

    //Wiederholungen Beine
    const repsLabel = document.createElement("label");
    repsLabel.textContent = "Wiederholungen:";
    repsLabel.htmlFor = "legsReps" + (exerciseCount + 1);

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.id = "legsReps" + (exerciseCount + 1);
    repsInput.name = "legsReps" + (exerciseCount + 1);
    repsInput.min = "1";

    //Gewicht Beine
    const weightLabel = document.createElement("label");
    weightLabel.textContent = "Gewicht:";
    weightLabel.htmlFor = "legsWeight" + (exerciseCount + 1);

    const weightInput = document.createElement("input");
    weightInput.type = "number";
    weightInput.id = "legsWeight" + (exerciseCount + 1);
    weightInput.name = "legsWeight" + (exerciseCount + 1);
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

    exercise.appendChild(deleteButton);
    legsExercises.insertBefore(exercise, legsExercises.querySelector(".addExercise"));
}

function deleteExercise(exercise)
{
    exercise.remove();
}

function createDeleteButton(exercise)
{
    const deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.textContent = "Löschen";
    deleteButton.className = "deleteButton";

    deleteButton.onclick = function()
    {
        deleteExercise(exercise);
    };

    return deleteButton;
}

//-------------------------------------------bearbeitung workout-------------------------------------------
function loadSavedExercises()
{
    if (savedExercises.length === 0)
    {
        return;
    }

    let counts = {back: 1, chest: 1, arms: 1, shoulder: 1, legs: 1};
    for (const exerciseData of savedExercises)
    {
        const exerciseName = exerciseData[0];
        const sets = exerciseData[1];
        const reps = exerciseData[2];
        const weight = exerciseData[3];

        let category;
        if (exercises.back.includes(exerciseName))
        {
            category = "back";
        }
        else if (exercises.chest.includes(exerciseName))
        {
            category = "chest";
        }
        else if (exercises.arms.includes(exerciseName))
        {
            category = "arms";
        }
        else if (exercises.shoulder.includes(exerciseName))
        {
            category = "shoulder";
        }
        else if (exercises.legs.includes(exerciseName))
        {
            category = "legs";
        }

        if (category === "back")
        {
             if (counts.back === 1)
                {
                    addBackExercise();
                }

            const number = counts.back;

            document.getElementById("backExercise" + number).value = exerciseName;
            document.getElementById("backSets" + number).value = sets;
            document.getElementById("backReps" + number).value = reps;
            document.getElementById("backWeight" + number).value = weight;

            counts.back++;

            if (counts.back <= savedExercises.filter(exercise => exercises.back.includes(exercise[0])).length)
            {
                addBackExercise();
            }
        }

        else if (category === "chest")
        {
            if (counts.chest === 1)
                {
                    addChestExercise();
                }

            const number = counts.chest;

            document.getElementById("chestExercise" + number).value = exerciseName;
            document.getElementById("chestSets" + number).value = sets;
            document.getElementById("chestReps" + number).value = reps;
            document.getElementById("chestWeight" + number).value = weight;

            counts.chest++;

            if (counts.chest <= savedExercises.filter(exercise => exercises.chest.includes(exercise[0])).length)
            {
                addChestExercise();
            }
        }

        else if (category === "arms")
        {
            if (counts.arms === 1)
                {
                    addArmsExercise();
                }

            const number = counts.arms;

            document.getElementById("armsExercise" + number).value = exerciseName;
            document.getElementById("armsSets" + number).value = sets;
            document.getElementById("armsReps" + number).value = reps;
            document.getElementById("armsWeight" + number).value = weight;

            counts.arms++;

            if (counts.arms <= savedExercises.filter(exercise => exercises.arms.includes(exercise[0])).length)
            {
                addArmsExercise();
            }
        }

        else if (category === "shoulder")
        {
            if (counts.shoulder === 1)
                {
                    addShoulderExercise();
                }

            const number = counts.shoulder;

            document.getElementById("shoulderExercise" + number).value = exerciseName;
            document.getElementById("shoulderSets" + number).value = sets;
            document.getElementById("shoulderReps" + number).value = reps;
            document.getElementById("shoulderWeight" + number).value = weight;

            counts.shoulder++;

            if (counts.shoulder <= savedExercises.filter(exercise => exercises.shoulder.includes(exercise[0])).length)
            {
                addShoulderExercise();
            }
        }

        else if (category === "legs")
        {
            if (counts.legs === 1)
                {
                    addLegsExercise();
                }

            const number = counts.legs;

            document.getElementById("legsExercise" + number).value = exerciseName;
            document.getElementById("legsSets" + number).value = sets;
            document.getElementById("legsReps" + number).value = reps;
            document.getElementById("legsWeight" + number).value = weight;

            counts.legs++;

            if (counts.legs <= savedExercises.filter(exercise => exercises.legs.includes(exercise[0])).length)
            {
                addLegsExercise();
            }
        }
    }
}

loadSavedExercises();