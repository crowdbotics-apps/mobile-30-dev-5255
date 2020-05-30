import { combineReducers } from "redux";

/**
 * You can import more reducers here
 */


//@BlueprintReduxImportInsertion
import EmailAuth4896Reducer from '../features/EmailAuth4896/redux/reducers';
import EmailAuth4895Reducer from '../features/EmailAuth4895/redux/reducers';
import EmailAuth4890Reducer from '../features/EmailAuth4890/redux/reducers';

export const combinedReducers = combineReducers({
  blank: (state, action) => {
    if (state == null) state = [];
    return state;
  },


  //@BlueprintReduxCombineInsertion
EmailAuth4896: EmailAuth4896Reducer,
EmailAuth4895: EmailAuth4895Reducer,
EmailAuth4890: EmailAuth4890Reducer,

});