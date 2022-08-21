import { useEffect, useState } from 'react';
import styles from './DirItem.module.scss';
import axios from '../config/axios';
import moment from 'moment';

//importing icons
import { FiMoreHorizontal } from 'react-icons/fi';
import { Button, Popover } from 'antd';


const DirItem = ({ item, dir, setDir }) => {
    const [stat, setStat] = useState([]);
    const [type, setType] = useState('');

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

    const handleClickEvent = () => {
        if (type === 'folder') {
            setDir(dir + '/' + item);
        } else {
            axios.post(`/file-manager/open-file?path=${dir}/${item}`);
        }
    }

    return (
        <tr className={styles.dirItem} onClick={handleClickEvent}>
            <td style={{ width: '500px' }}>{item}</td>
            <td style={{ width: '300px' }}>
                {moment(stat.st_mtime).format('MMMM DD Y - LT')}
            </td>
            <td>
                {item.substring(1).includes('.') ? item.split('.')[item.split('.').length - 1] + ' File' : 'Folder'}
            </td>
            <td>{type === 'file' ? bytesToSize(stat.st_size) : '-'}</td>
            <td>
                <Popover content={
                    <div className={styles.actions}>
                        <span style={{ marginBottom: '1rem', display: 'block' }}>Copy {type}</span>

                        <span>Move {type}</span>
                    </div>
                } title="Actions">
                    <FiMoreHorizontal size={20} />
                </Popover>
            </td>
        </tr>
    );
};

export default DirItem;