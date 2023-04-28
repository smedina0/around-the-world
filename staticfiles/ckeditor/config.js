CKEDITOR.editorConfig = function (config) {
  // Add the alignment buttons to the toolbar
  config.toolbarGroups = [
    // ...
    { name: 'align', groups: ['align'] },
    // ...
  ];

  // Make sure the alignment commands are included
  config.extraPlugins = 'justify';

  // Other configuration options can go here as well
};
