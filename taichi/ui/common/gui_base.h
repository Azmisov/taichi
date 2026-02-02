#pragma once
#include <string>
#include <vector>
#include "taichi/ui/utils/utils.h"

namespace taichi::ui {

class GuiBase {
 public:
  virtual void begin(const std::string &name,
                     float x,
                     float y,
                     float width,
                     float height,
                     bool movable = true,
                     bool resizable = true,
                     bool collapsible = true) = 0;
  virtual void end() = 0;
  virtual void text(const std::string &text) = 0;
  virtual void text(const std::string &text, glm::vec3 color) = 0;
  virtual bool checkbox(const std::string &name, bool old_value) = 0;
  virtual int slider_int(const std::string &name,
                         int old_value,
                         int minimum,
                         int maximum) = 0;
  virtual float slider_float(const std::string &name,
                             float old_value,
                             float minimum,
                             float maximum) = 0;
  virtual glm::vec3 color_edit_3(const std::string &name,
                                 glm::vec3 old_value) = 0;
  virtual bool button(const std::string &text) = 0;
  virtual int combo(const std::string &label,
                    int current_item,
                    const std::vector<const char *> &items) = 0;
  virtual int input_int(const std::string &label, int old_value) = 0;
  virtual float input_float(const std::string &label, float old_value) = 0;
  virtual int drag_int(const std::string &label,
                       int old_value,
                       float speed,
                       int minimum,
                       int maximum) = 0;
  virtual float drag_float(const std::string &label,
                           float old_value,
                           float speed,
                           float minimum,
                           float maximum) = 0;
  virtual bool tree_node_push(const std::string &label) = 0;
  virtual void tree_node_pop() = 0;
  virtual void separator() = 0;
  virtual void same_line() = 0;
  virtual void indent() = 0;
  virtual void unindent() = 0;
  virtual void progress_bar(float fraction) = 0;
  virtual void prepare_for_next_frame() = 0;
  virtual ~GuiBase() = default;
};

}  // namespace taichi::ui
