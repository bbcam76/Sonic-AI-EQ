import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';
import NotFoundPage from './pages/NotFoundPage';
import ResultsPage from './pages/ResultsPage';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={HomePage} />
                <Route path="/upload" component={UploadPage} />
                <Route path="/results" component={ResultsPage} />
                <Route component={NotFoundPage} />
            </Switch>
        </Router>
    );
};

export default App;

