/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        fontFamily: {
            // Default sequences
            'serif': ['DM Serif Text','EB Garamond','ui-serif'],
            'sans': ['Work Sans','Nunito Sans','ui-sans-serif'],
            // Simple Charity fonts
            'garamond': ['EB Garamond'],
            'nunito': ['Nunito Sans'],
            'dmserif': ['DM Serif Text'],
            'work': ['Work Sans'],
        },
        extend: {
            colors: {
                'coral': '#ff7f50',
                'apricot': '#ffb78f',
                'cream': '#fae1c8',
                'dusk': '#263b4e',
                'midnight': '#031928',
                'cloud': '#f0f0f0',
                'zeal': '#098c93',
                'canary': '#ffc32e',
                'mint': '#c6e0c5',
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
