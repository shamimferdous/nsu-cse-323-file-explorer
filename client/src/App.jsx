import axios from './config/axios';
import { useEffect, useState } from 'react';
import styles from './App.module.scss';

//importing components
import { FcFolder } from 'react-icons/fc';
import { MdChevronRight } from 'react-icons/md';
import { VscRefresh } from 'react-icons/vsc';
import { HiOutlineChevronLeft } from 'react-icons/hi';
import DirItem from './Components/DirItem';
import { Button } from 'antd';

function App() {

    const [dir, setDir] = useState('');
    const [dirItems, setDirItems] = useState([]);
    const [refresh, setRefresh] = useState(null);
    const [copyPath, setCopyPath] = useState(null);
    const [movePath, setMovePath] = useState(null);

    useEffect(() => {
        axios.get(`/file-manager/get-directory`, {
            params: {
                dir: dir ? dir : null
            }
        }).then(response => {
            // console.log(response.data);
            setDir(response.data.dir);
            setDirItems(response.data.list);
        })
    }, [dir, refresh]);

    const handleDirBackEvent = () => {
        let dirArr = dir.split('/');
        dirArr.pop();
        setDir(dirArr.join('/'));
    }

    const handleCopyEvent = () => {
        let dirItemName = copyPath.split('/')[copyPath.split('/').length - 1];
        axios.post(`/file-manager/copy`, {}, {
            params: {
                original_path: copyPath,
                destination_path: dir + '/' + dirItemName
            }
        }).then(response => {
            setRefresh(Math.random());
            setCopyPath(null);
        })
    }


    const handleMoveEvent = () => {
        let dirItemName = movePath.split('/')[movePath.split('/').length - 1];
        axios.post(`/file-manager/move`, {}, {
            params: {
                original_path: movePath,
                destination_path: dir + '/' + dirItemName
            }
        }).then(response => {
            setRefresh(Math.random());
            setMovePath(null);
        })
    }

    return (
        <div className={styles.container}>

            {/* <img src="/el-1.svg" alt="" className={styles.el_1} />
            <img src="/el-2.svg" alt="" className={styles.el_2} /> */}

            <section className={styles.body}>
                <div className={styles.header}>
                    <div className={styles.dir}>
                        <img src="https://cdn-icons-png.flaticon.com/512/2292/2292038.png" alt="" />
                        {
                            dir.split('/').map((dirFolder, index) => {
                                return <span key={index}>
                                    {dirFolder}
                                    {
                                        index !== dir.split('/').length - 1 ?
                                            <MdChevronRight size={15} />
                                            :
                                            null
                                    }
                                </span>
                            })
                        }

                        <VscRefresh onClick={() => setRefresh(Math.random())} size={20} className={styles.refresh} />

                    </div>
                </div>

                <div className={styles.dir_details}>
                    <FcFolder size={80} />
                    <div className={styles.dir_details__right}>
                        <div style={{ display: 'flex', alignItems: 'center' }}>
                            {
                                dir.split('/').length > 2 &&
                                <HiOutlineChevronLeft
                                    size={25}
                                    style={{ marginRight: '.2rem', marginTop: '.25rem', cursor: 'pointer' }} onClick={handleDirBackEvent}
                                />
                            }
                            <strong>{dir.split('/')[dir.split('/').length - 1]}</strong>
                            {
                                copyPath &&
                                <Button onClick={handleCopyEvent} style={{ marginLeft: '1rem', marginTop: '.5rem' }} type="dashed">paste {copyPath.split('/')[copyPath.split('/').length - 1]}</Button>
                            }
                            {
                                movePath &&
                                <Button onClick={handleMoveEvent} style={{ marginLeft: '1rem', marginTop: '.5rem' }} type="dashed">move {movePath.split('/')[movePath.split('/').length - 1]}</Button>
                            }
                        </div>
                        <span>{dirItems.length} Items</span>
                    </div>
                </div>

                <table>
                    <thead>
                        <tr>
                            <th style={{ width: '500px' }}>Name</th>
                            <th style={{ width: '300px' }}>Modified</th>
                            <th>Type</th>
                            <th>Size</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            dirItems.map((item, index) => {
                                return <DirItem
                                    key={index}
                                    item={item}
                                    dir={dir}
                                    setDir={setDir}
                                    setRefresh={setRefresh}
                                    setCopyPath={setCopyPath}
                                    setMovePath={setMovePath}
                                />
                            })
                        }
                    </tbody>
                </table>
            </section>
        </div>
    );
}

export default App;
