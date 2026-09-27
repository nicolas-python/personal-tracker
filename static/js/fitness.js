//-------------------------------------------create_workout.html-------------------------------------------
function addExercise() {

    const exercises = document.getElementById("exercises");
    const exerciseCount = exercises.children.length;

    const exercise = document.createElement("div");
    exercise.className = "exercise";

    const label = document.createElement("label");
    label.textContent = "Übung " + (exerciseCount + 1) + ":";
    label.htmlFor = "exercise" + (exerciseCount + 1);

    const select = document.createElement("select");
    select.id = "exercise" + (exerciseCount + 1);
    select.name = "exercise" + (exerciseCount + 1);

    const firstSelect = document.getElementById("exercise1");

    for (const option of firstSelect.options)
        {select.add(option.cloneNode(true));}

    exercise.appendChild(label);
    exercise.appendChild(select);
    exercises.appendChild(exercise);
}