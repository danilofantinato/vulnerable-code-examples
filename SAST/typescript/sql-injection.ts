import { executeQuery } from 'database';

const userId = '1';
const query = 'SELECT * FROM users WHERE id = ?';
executeQuery(query, [userId]);