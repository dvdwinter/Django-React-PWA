import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga';
import { logger } from 'redux-logger';

import rootReducer from '../reducers/rootReducer';
import rootSaga from '../sagas';


export default function configureStore() {
  const sagaMiddleware = createSagaMiddleware();
  sagaMiddleware.run(rootSaga);

  return createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
    applyMiddleware(sagaMiddleware, logger),
  );
}
