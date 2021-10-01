import React from "react";
import "antd/dist/antd.css";
import "./index.css";
import { Tag, Tooltip, Form, Input, Button, InputNumber } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";

const GameCreationPage = () => {
  const onFinish = (values) => {
    console.log("Success:", values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  //tags
  const [tags, setTags] = React.useState(["Games"]);
  const [inputValue, setInputValue] = React.useState("");
  const [inputVisible, setInputVisible] = React.useState(false);
  const [editInputIndex, setEditInputIndex] = React.useState(-1);
  const [editInputValue, setEditInputValue] = React.useState("");
  const inputRef = React.useRef();
  const saveEditInputRef = React.useRef();

  const showInput = () => {
    setInputVisible(true);
    setTimeout(() => {
      if (inputRef.current) {
        inputRef.current.focus();
      }
    });
  };

  const handleInputChange = (value) => {
    setInputValue(value);
  };

  const handleEditInputChange = (value) => {
    setEditInputValue(value);
  };

  const handleInputConfirm = () => {
    if (inputValue && tags.indexOf(inputValue) === -1) {
      setTags([...tags, inputValue]);
    }
    setInputValue("");
    setInputVisible(false);
  };

  const handleEditInputConfirm = () => {
    const newTags = [...tags];
    newTags[editInputIndex] = editInputValue;
    setTags(newTags);
    setEditInputIndex(-1);
    setEditInputValue("");
  };

  const handleClose = (removeTag) => {
    const newTags = tags.filter((tag) => tag !== removeTag);
    setTags(newTags);
  };

  return (
    <div className="creation-page-container">
      <div className="creation-page-header-container">
        <h2 className="creation-page-heading">Game Creation!</h2>
      </div>
      <div className="info-container">
        <p className="text">
          Hi <span className="text-highlight">James</span>,
        </p>
        <p className="text">
          Please complete the following to proceed with the creation of your
          game.
        </p>
        <Form
          name="basic"
          labelCol={{
            span: 8,
          }}
          wrapperCol={{
            span: 10,
          }}
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="GAME NAME: "
            name="Game Name"
            rules={[
              {
                required: true,
              },
            ]}
          >
            <Input placeholder="Enter name of the Game" />
          </Form.Item>

          <Form.Item
            label="DESCRIPTION"
            name="Game Description"
            rules={[
              {
                required: true,
              },
            ]}
          >
            <Input placeholder="Enter Game Description" />
          </Form.Item>

          <Form.Item label="NUMBER OF QUIZZES: ">
            <Form.Item
              name="Number of Quizzes"
              noStyle
              rules={[
                {
                  required: true,
                },
              ]}
            >
              <InputNumber min={1} max={5} />
            </Form.Item>
            <span className="ant-form-text"></span>
          </Form.Item>

          <Form.Item label="NUMBER 0F QUESTIONS PER QUIZ: ">
            <Form.Item
              name="Number of Questions"
              noStyle
              rules={[
                {
                  required: true,
                },
              ]}
            >
              <InputNumber min={1} max={10} />
            </Form.Item>
            <span className="ant-form-text"></span>
          </Form.Item>

          {/* <Form.Item
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          > */}
          <Form.Item label="ENTER RELEVANT GAME TAGS">
            <div>
              {tags.map((tag, index) => {
                if (editInputIndex === index) {
                  return (
                    <Input
                      ref={saveEditInputRef}
                      key={tag}
                      size="small"
                      className="tag-input"
                      value={editInputValue}
                      onChange={(e) => handleEditInputChange(e.target.value)}
                      onBlur={handleEditInputConfirm}
                      onPressEnter={handleEditInputConfirm}
                    />
                  );
                }
                const isLongTag = tag.length > 20;

                const tagElem = (
                  <Tag
                    className="edit-tag"
                    key={tag}
                    closable={index !== 0}
                    onClose={() => handleClose(tag)}
                  >
                    <span
                      onDoubleClick={(e) => {
                        if (index !== 0) {
                          setEditInputIndex(index);
                          setEditInputValue(tag);
                          setTimeout(() => {
                            if (saveEditInputRef.current) {
                              saveEditInputRef.current.focus();
                            }
                          });
                          e.preventDefault();
                        }
                      }}
                    >
                      {isLongTag ? `${tag.slice(0, 20)}...` : tag}
                    </span>
                  </Tag>
                );
                return isLongTag ? (
                  <Tooltip title={tag} key={tag}>
                    {tagElem}
                  </Tooltip>
                ) : (
                  tagElem
                );
              })}

              {inputVisible && (
                <Input
                  ref={inputRef}
                  type="text"
                  size="small"
                  className="tag-input"
                  value={inputValue}
                  onChange={(e) => handleInputChange(e.target.value)}
                  onBlur={handleInputConfirm}
                  onPressEnter={handleInputConfirm}
                />
              )}
              {!inputVisible && (
                <Tag className="site-tag-plus" onClick={showInput}>
                  <PlusOutlined /> New Tag
                </Tag>
              )}
            </div>
          </Form.Item>

          <hr></hr>
          <div className="button">
            <Button type="primary" htmlType="Back" className="backBtn">
              <Link to={"/games"}>Back</Link>
            </Button>
            <Button type="primary" htmlType="Next" className="nextBtn">
              <Link to={"/editquiz"}>Next</Link>
            </Button>
          </div>
          {/* </Form.Item> */}
        </Form>
      </div>
    </div>
  );
};

export default GameCreationPage;
