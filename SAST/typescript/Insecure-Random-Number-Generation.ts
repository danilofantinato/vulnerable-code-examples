// File: sample.ts

import { randomBytes } from 'crypto';

const secureRandomBuffer = randomBytes(4);
const secureRandomNumber = parseInt(secureRandomBuffer.toString('hex'), 16);
console.log(`Secure random number: ${secureRandomNumber}`);