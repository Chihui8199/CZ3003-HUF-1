import yelp from '../../yelp';

export const fetchGames = async () => {
  try {
    const response = await yelp.get('/hufgames', {});
    return response;
  } catch (err) {
    return err.message;
  }
};

export const fetchQuizzes = async (game_id) => {
  try {
    const response = await yelp.get('/hufquiz', { params: { game_id } });
    return response;
  } catch (err) {
    return err.message;
  }
};

export const createGame = async (
  username,
  game_name,
  game_tag,
  no_of_quiz,
  game_description,
  total_no_qn
) => {
  try {
    const response = await yelp.post('/hufgames/', {
      username,
      game_name,
      game_tag,
      no_of_quiz,
      game_description,
      total_no_qn,
    });
    return response;
  } catch (err) {
    return err.message;
  }
};


// api function to call 'localhost:8000/hufquiz'
export const fetchQuizQuestions = async (quiz_id) => {
  try {
    const response = await yelp.get('/hufquizqn', { params: { quiz_id } });
    return response;
  } catch (err) {
    return err.message;
  }
};

// api function to call 'localhost:8000/hufquiz'
export const fetchQuizResult = async () => {
  try {
    const response = await yelp.get('/hufquizresult', {});
    return response;
  } catch (err) {
    return err.message;
  }
};

export const fetchQuizLeaderBoard = async (quiz_id) => {
  try {
    const response = await yelp.post('/quiztopfive/', { quiz_id });
    return response;
  } catch (err) {
    return err.message;
  }
};
