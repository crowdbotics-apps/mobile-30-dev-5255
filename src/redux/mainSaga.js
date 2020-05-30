import { all, takeEvery, take } from "redux-saga/effects";


//@BlueprintReduxSagaImportInsertion
import EmailAuth4896Saga from '../features/EmailAuth4896/redux/sagas';
import EmailAuth4895Saga from '../features/EmailAuth4895/redux/sagas';
import EmailAuth4890Saga from '../features/EmailAuth4890/redux/sagas';

function* helloSaga() {
  console.log("Hello from saga!");
}

export function* mainSaga() {
  yield all([
    takeEvery("TEST/ALO", helloSaga),
    // other sagas go here


    //@BlueprintReduxSagaMainInsertion
EmailAuth4896Saga,
EmailAuth4895Saga,
EmailAuth4890Saga,
    
  ]);
}