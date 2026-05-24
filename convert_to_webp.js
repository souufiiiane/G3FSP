const fs = require('fs');
const path = require('path');
const sharp = require('sharp'); // Requires running: npm install sharp

const itemsToConvert = [
    { input: 'Logo V1.3.png', output: 'Logo V1.3.webp' },
    { input: 'Projects/Restauration de la Mosquée de Tinmel.jpeg', output: 'Projects/Restauration de la Mosquée de Tinmel.webp' },
    { input: 'Projects/Stabilisation de Talus à Nador.jpeg', output: 'Projects/Stabilisation de Talus à Nador.webp' }
];

async function convertAll() {
    for (const item of itemsToConvert) {
        const inputPath = path.join(__dirname, item.input);
        const outputPath = path.join(__dirname, item.output);

        if (fs.existsSync(inputPath)) {
            try {
                await sharp(inputPath)
                    .webp({ quality: 80 })
                    .toFile(outputPath);
                console.log(`Converted ${item.input} to WebP!`);
            } catch (err) {
                console.error(`Error converting ${item.input}:`, err);
            }
        } else {
            console.log(`File not found: ${item.input}`);
        }
    }
}

convertAll();
