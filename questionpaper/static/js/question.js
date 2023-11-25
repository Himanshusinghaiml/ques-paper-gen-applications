$(document).ready(function () {
    let currentQuestionId = 0; // Initialize with the first question's ID
    var size;
    function loadQuestion(questionId) {
        $.ajax({
            url: `/get_next_question/${questionId}/`,
            method: 'GET',
            success: function (data) {
                if (data.question_text) { 
                    $('#question_no').next('label').text(data.id);
                    $('#question-text').text(`Question ${data.id}: ${data.question_text}`);
                    $('#difficulty').text(`Difficulty: ${data.difficulty}`);
                    $('#marks').text(`Marks: ${data.marks}`);
                    
                    size = data.size;
                } else {
                    alert('Question is not in database ! try to contact organization ');
                
            }
            },
            error: function () {
                alert('Failed to load the question.');
            }
        });
    }

    $('#next-button').click(function () {
        if(currentQuestionId<size-1){
            currentQuestionId += 1;
            loadQuestion(currentQuestionId);
        }
        else{
            alert("Question ended ");
        }
         
    });

    $('#prev-button').click(function () {
        if (currentQuestionId >= 1) {
            currentQuestionId -= 1;
            loadQuestion(currentQuestionId);
        } else {
            alert('This is the first question.');
        }
    });

    // Load the initial question
    loadQuestion(currentQuestionId);
});