import { useEffect, useState } from 'react';
import styles from './DirItem.module.scss';
import axios from '../config/axios';
import moment from 'moment';

//importing icons
import { FiMoreHorizontal } from 'react-icons/fi';
import { Button, Input, Popover } from 'antd';


const DirItem = ({ item, dir, setDir, setRefresh, setCopyPath, setMovePath }) => {
    const [stat, setStat] = useState([]);
    const [type, setType] = useState('');
    const [showRename, setShowRename] = useState(false);

    function bytesToSize(bytes) {
        var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        if (bytes == 0) return '0 Byte';
        var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
        return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
    }

    useEffect(() => {
        setType(item.substring(1).includes('.') ? 'file' : 'folder');
        axios.get(`/file-manager/path-stat?path=${dir}/${item}`).then(response => {
            setStat(response.data);
        })
    }, [item]);

    const handleClickEvent = e => {
        switch (e.detail) {
            case 1:
                break;
            case 2:
                if (type === 'folder') {
                    setDir(dir + '/' + item);
                } else {
                    axios.post(`/file-manager/open-file?path=${dir}/${item}`);
                }
                break;
            case 3:
                console.log("triple click");
                break;
            default:
                break;
        }

    }

    const renameDirItem = newName => {
        axios.post(`/file-manager/rename`, {}, {
            params: {
                old_path: dir + "/" + item,
                new_path: dir + "/" + newName,
            }
        }).then(response => {
            setRefresh(Math.random());
            setShowRename(false);
        });
    }

    return (
        <tr className={styles.dirItem} onClick={handleClickEvent}>
            <td style={{ width: '500px' }}>
                {
                    showRename ?
                        <Input defaultValue={item} onPressEnter={(e) => renameDirItem(e.target.value)} />
                        :
                        <span className={styles.dirItemName}>{item}</span>
                }
            </td>
            <td style={{ width: '300px' }}>
                {/* {moment(stat.st_birthtime).format('MMM DD YYYY - LT')} */}
                {moment(stat.st_mtime).format('MMM DD YYYY - LT')}
            </td>
            <td>
                {item.substring(1).includes('.') ? item.split('.')[item.split('.').length - 1] + ' File' : 'Folder'}
            </td>
            <td>{type === 'file' ? bytesToSize(stat.st_size) : '-'}</td>
            <td>
                <Popover content={
                    <div className={styles.actions}>
                        <span onClick={() => setShowRename(true)} style={{ marginTop: '0rem' }}>Rename {type}</span>

                        <span onClick={() => setCopyPath(dir + "/" + item)}>Copy {type}</span>

                        <span onClick={() => setMovePath(dir + "/" + item)}>Move {type}</span>

                    </div>
                } title="Actions">
                    <FiMoreHorizontal size={20} />
                </Popover>
            </td>
        </tr>
    );
};

export default DirItem;