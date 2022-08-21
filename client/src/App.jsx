import axios from './config/axios';
import { useEffect } from 'react';
import styles from './App.module.scss';

function App() {

    useEffect(() => {
        axios.get(`/file-manager/get-directory`).then(response => {
            console.log(response);
        })
    }, []);

    return (
        <div className={styles.container}>
            <section className={styles.body}>

            </section>
        </div>
    );
}

export default App;
